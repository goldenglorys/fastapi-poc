import os
import time

import psutil
from fastapi import APIRouter

from .schemas import DiskUsage, HealthStatus, SystemResources

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

start_time = time.time()
process = psutil.Process(os.getpid())


@router.get(
    "/",
    summary="Get Health Status",
    description="Get the health status of the application",
    response_description="Application health status",
    response_model=HealthStatus,
)
def get_health_status() -> HealthStatus:
    """Returns the current health status of the system.

    Returns:
        A dictionary containing the status, uptime, system resource usage, and application version.
    """
    current_time = time.time()
    uptime = current_time - start_time
    cpu_percent = psutil.cpu_percent()
    memory_info = process.memory_info()
    disk_usage = psutil.disk_usage("/")

    return HealthStatus(
        application_version="0.1.0",
        status="OK",
        uptime_seconds=uptime,
        system_resources=SystemResources(
            cpu_usage_percent=cpu_percent,
            disk_usage=DiskUsage(
                free_mb=disk_usage.free / (1024 * 1024),
                total_mb=disk_usage.total / (1024 * 1024),
                used_mb=disk_usage.used / (1024 * 1024),
            ),
            memory_usage_mb=memory_info.rss / (1024 * 1024),
        ),
    )