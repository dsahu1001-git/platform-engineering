# Environment Promotion and Test Plan

This platform runs multiple logical environments on one EKS cluster by isolating each environment into its own namespace:

- `release-control-dev`
- `release-control-stage`
- `release-control-prod`

The DevOps repo owns the environment definitions, release intent, promotion policy, test plans, observability defaults, and generated Kubernetes assets. Application repos own only application code and Dockerfiles.

## Promotion Flow

1. Service CI publishes immutable images to ECR.
2. Dev release intent references the image selected for integration testing.
3. Promotion to stage copies the approved version from dev to `delivery/releases/stage.yaml`.
4. Promotion to prod copies the approved version from stage to `delivery/releases/prod.yaml`.
5. Argo CD or Harness CD reconciles the target namespace from the platform repo.

## Required Gates

Every promotion must pass:

- Platform catalog validation.
- Release intent validation.
- Smoke tests.
- API contract tests.
- Observability tests.
- Release evidence capture.

Production additionally requires:

- Production readiness test plan.
- Human approval.
- SLO and policy evidence.

## Test Plans

Test plans live in `delivery/test-plans/` so service teams can discover expectations without editing deployment machinery.

- `release-control-smoke.yaml`: frontend availability, backend health, database health.
- `release-control-contract.yaml`: API status and logs response contract.
- `release-control-observability.yaml`: metrics and log endpoint verification.
- `release-control-prod-readiness.yaml`: production-only evidence and approval-policy checks.

## Harness Pipelines

- `release-control-enterprise-delivery`: the primary branched enterprise parent pipeline. It chains reusable child pipelines for frontend CI, backend CI, dev verification, environment promotion, approvals, and release evidence in one graph.
- `release-control-frontend-ci`: JavaScript CI with dependency governance, tests, build, and ECR publish.
- `release-control-backend-ci`: Python CI with dependency governance, contract tests, and ECR publish.
- `release-control-dev-cd`: dev release verification and evidence.
- `release-control-environment-promotion`: reusable environment promotion pipeline for dev -> stage and stage -> prod.

The primary pipeline branches by `release_path`:

- `dev_only`: CI, image publish, dev verification, evidence.
- `dev_to_stage`: CI, image publish, dev verification, stage approval, stage gates, evidence.
- `stage_to_prod`: CI, image publish, dev verification, production approval, production readiness, evidence.
- `full`: CI, image publish, dev verification, stage approval, stage gates, production approval, production readiness, evidence.

Harness runs these pipelines on the `platform-eks-dev` delegate inside the EKS cluster.
