# Harness Setup

Use Harness SaaS with Harness Cloud build infrastructure for the first PoC.

Required connectors:

- GitHub connector for all three repos.
- AWS connector for ECR and infrastructure workflows.
- Kubernetes connector after EKS exists.

Keep reusable templates in this repo. Avoid creating one-off pipelines per service.
