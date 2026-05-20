from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


REQUIRED = [
    "catalog/services/release-control-frontend.yaml",
    "catalog/services/release-control-backend.yaml",
    "delivery/releases/dev.yaml",
    "platform/environments/dev.yaml",
    "templates/kubernetes/base/deployment.yaml",
    "argocd/applicationsets/services.yaml",
    "harness/templates/ci/service-ci-template.yaml",
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

    checks = {
        "frontend runtime is javascript": "runtime: javascript" in frontend,
        "backend runtime is python": "runtime: python" in backend,
        "backend declares postgres": "postgres:" in backend,
        "backend declares metrics path": "metricsPath: /metrics" in backend,
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
