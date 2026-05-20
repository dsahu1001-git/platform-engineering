variable "name" {
  type = string
}

variable "environment" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
}

variable "vpc_cidr" {
  type = string
}

resource "random_password" "master" {
  length  = 24
  special = true
}

resource "aws_security_group" "postgres" {
  name        = "${var.name}-${var.environment}-postgres"
  description = "PostgreSQL access for ${var.name} ${var.environment}"
  vpc_id      = var.vpc_id

  ingress {
    description = "PostgreSQL from VPC"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_subnet_group" "this" {
  name       = "${var.name}-${var.environment}"
  subnet_ids = var.subnet_ids
}

resource "aws_db_instance" "this" {
  identifier             = "${var.name}-${var.environment}"
  engine                 = "postgres"
  engine_version         = "16"
  instance_class         = "db.t4g.micro"
  allocated_storage      = 20
  db_name                = "release_control"
  username               = "release_control"
  password               = random_password.master.result
  db_subnet_group_name   = aws_db_subnet_group.this.name
  vpc_security_group_ids = [aws_security_group.postgres.id]
  skip_final_snapshot    = true
  deletion_protection    = false
  publicly_accessible    = false
  storage_encrypted      = true
}

resource "aws_secretsmanager_secret" "database_url" {
  name = "${var.name}/${var.environment}/database-url"
}

resource "aws_secretsmanager_secret_version" "database_url" {
  secret_id = aws_secretsmanager_secret.database_url.id
  secret_string = jsonencode({
    DATABASE_URL = "postgresql://${aws_db_instance.this.username}:${random_password.master.result}@${aws_db_instance.this.address}:5432/${aws_db_instance.this.db_name}"
  })
}

output "secret_arn" {
  value = aws_secretsmanager_secret.database_url.arn
}

output "endpoint" {
  value = aws_db_instance.this.endpoint
}
