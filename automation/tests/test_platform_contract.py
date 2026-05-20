from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_initial_services_are_registered():
    assert (ROOT / "catalog/services/release-control-frontend.yaml").exists()
    assert (ROOT / "catalog/services/release-control-backend.yaml").exists()


def test_backend_declares_postgres_dependency():
    service = (ROOT / "catalog/services/release-control-backend.yaml").read_text()
    assert "postgres:" in service
    assert "databaseName: release_control" in service
