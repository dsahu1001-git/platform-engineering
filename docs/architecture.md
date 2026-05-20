# Architecture

The platform uses three repositories:

- `release-control-frontend`: JavaScript application code only.
- `release-control-backend`: Python application code only.
- `platform-engineering`: central platform product for infra, GitOps, CI/CD orchestration, monitoring, policy, and release governance.

## Runtime Flow

1. Harness CI checks out application repos.
2. Harness tests and builds container images.
3. Harness pushes images to ECR.
4. Harness updates release intent in `platform-engineering`.
5. Argo CD reconciles generated Kubernetes state into EKS.
6. AWS Load Balancer Controller exposes the public ALB endpoint.
7. Prometheus and Loki collect metrics and logs.
8. Release Control displays health, logs, metrics, versions, and PostgreSQL status.

## Data Layer

The backend uses PostgreSQL. The app repo only declares that it needs `DATABASE_URL`; the platform repo owns provisioning, secrets, network access, and environment-specific database class.
