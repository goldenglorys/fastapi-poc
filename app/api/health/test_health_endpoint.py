from app.main import app
from fastapi.testclient import TestClient

from .schemas import HealthStatus

client = TestClient(app)


def test_get_health_status():
    response = client.get("/health/")
    assert response.status_code == 200
    health_status = HealthStatus(**response.json())

    # Check if the required fields are present in the response
    assert "application_version" in health_status.dict()
    assert "status" in health_status.dict()
    assert "uptime_seconds" in health_status.dict()
    assert "system_resources" in health_status.dict()

    # Check if the system_resources field has the required fields
    system_resources = health_status.system_resources
    assert "cpu_usage_percent" in system_resources.dict()
    assert "disk_usage" in system_resources.dict()
    assert "memory_usage_mb" in system_resources.dict()

    # Check if the disk_usage field has the required fields
    disk_usage = system_resources.disk_usage
    assert "free_mb" in disk_usage.dict()
    assert "total_mb" in disk_usage.dict()
    assert "used_mb" in disk_usage.dict()

    # Check if the data types are as expected
    assert isinstance(health_status.application_version, str)
    assert isinstance(health_status.status, str)
    assert isinstance(health_status.uptime_seconds, float)

    assert isinstance(system_resources.cpu_usage_percent, float)
    assert isinstance(system_resources.memory_usage_mb, float)

    assert isinstance(disk_usage.free_mb, float)
    assert isinstance(disk_usage.total_mb, float)
    assert isinstance(disk_usage.used_mb, float)
