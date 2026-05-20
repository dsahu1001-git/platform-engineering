output "cluster_name" {
  value = module.eks.cluster_name
}

output "ecr_repositories" {
  value = module.ecr.repository_urls
}

output "postgres_secret_arn" {
  value     = module.postgres.secret_arn
  sensitive = true
}

output "postgres_endpoint" {
  value     = module.postgres.endpoint
  sensitive = true
}
