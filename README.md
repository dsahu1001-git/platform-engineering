# Platform Engineering

Central enterprise delivery platform repository.

This repo is the platform product that turns service metadata and release intent into secure, observable, governed deployments.

It owns:

- AWS infrastructure as Terraform.
- EKS platform add-ons.
- PostgreSQL provisioning patterns.
- Argo CD GitOps bootstrap and ApplicationSets.
- Harness templates and platform pipelines.
- Service catalog and release intent.
- Observability dashboards, alerts, and SLO templates.
- Security and policy guardrails.

Application repositories contain application code only.

## Initial Application Repos

- `release-control-frontend`: JavaScript frontend.
- `release-control-backend`: Python backend with PostgreSQL dependency.

## Safety

This repository is prepared for planning and validation. Do not run Terraform apply until the infrastructure creation step is explicitly approved.
