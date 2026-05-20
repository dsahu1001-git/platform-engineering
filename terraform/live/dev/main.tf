terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "network" {
  source      = "../../modules/network"
  name        = var.platform_name
  environment = var.environment
  cidr_block  = var.vpc_cidr
}

module "eks" {
  source          = "../../modules/eks"
  name            = var.platform_name
  environment     = var.environment
  vpc_id          = module.network.vpc_id
  private_subnets = module.network.private_subnet_ids
}

module "ecr" {
  source       = "../../modules/ecr"
  repositories = ["release-control-frontend", "release-control-backend"]
}

module "postgres" {
  source      = "../../modules/postgres"
  name        = "release-control"
  environment = var.environment
  vpc_id      = module.network.vpc_id
  subnet_ids  = module.network.private_subnet_ids
  vpc_cidr    = var.vpc_cidr
}
