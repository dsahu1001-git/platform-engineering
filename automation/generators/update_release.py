import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(description="Update release intent for a service.")
    parser.add_argument("--environment", required=True)
    parser.add_argument("--service", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--digest", default="")
    args = parser.parse_args()

    release_file = ROOT / "delivery" / "releases" / f"{args.environment}.yaml"
    if not release_file.exists():
        raise SystemExit(f"Release file does not exist: {release_file}")

    print(
        "Release update requested. In production this script should perform a structured YAML update "
        "and open a governed PR."
    )
    print(f"environment={args.environment}")
    print(f"service={args.service}")
    print(f"version={args.version}")
    print(f"tag={args.tag}")
    print(f"digest={args.digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
