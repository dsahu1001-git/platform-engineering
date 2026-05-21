from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


REQUIRED = [
    "catalog/services/release-control-frontend.yaml",
    "catalog/services/release-control-backend.yaml",
    "delivery/releases/dev.yaml",
    "delivery/releases/stage.yaml",
    "delivery/releases/prod.yaml",
    "delivery/test-plans/release-control-smoke.yaml",
    "delivery/test-plans/release-control-contract.yaml",
    "delivery/test-plans/release-control-observability.yaml",
    "delivery/test-plans/release-control-prod-readiness.yaml",
    "platform/environments/dev.yaml",
    "platform/environments/stage.yaml",
    "platform/environments/prod.yaml",
    "generated/kubernetes/environments.yaml",
    "templates/kubernetes/base/deployment.yaml",
    "argocd/applicationsets/services.yaml",
    "harness/templates/ci/service-ci-template.yaml",
    "harness/pipelines/release-control-environment-promotion.yaml",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing required platform files:")
        for path in missing:
            print(f"- {path}")
        return 1

    frontend = (ROOT / "catalog/services/release-control-frontend.yaml").read_text()
    backend = (ROOT / "catalog/services/release-control-backend.yaml").read_text()
    stage_release = (ROOT / "delivery/releases/stage.yaml").read_text()
    prod_release = (ROOT / "delivery/releases/prod.yaml").read_text()

    checks = {
        "frontend runtime is javascript": "runtime: javascript" in frontend,
        "backend runtime is python": "runtime: python" in backend,
        "backend declares postgres": "postgres:" in backend,
        "backend declares metrics path": "metricsPath: /metrics" in backend,
        "stage promotes from dev": "sourceEnvironment: dev" in stage_release,
        "prod promotes from stage": "sourceEnvironment: stage" in prod_release,
        "stage requires test plans": "requiredTestPlans:" in stage_release,
        "prod requires prod readiness": "release-control-prod-readiness" in prod_release,
    }

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("Catalog validation failed:")
        for name in failed:
            print(f"- {name}")
        return 1

    print("Platform catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
