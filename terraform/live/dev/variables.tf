variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "platform_name" {
  type    = string
  default = "enterprise-delivery-platform"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "vpc_cidr" {
  type    = string
  default = "10.42.0.0/16"
}
