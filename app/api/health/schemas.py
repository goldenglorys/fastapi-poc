from app.api.schemas import BaseAPISchema
from pydantic import Field


class DiskUsage(BaseAPISchema):
    """Represents disk usage information.

    Attributes:
        total_mb (float): Total disk space available in MB.
        used_mb (float): Amount of disk space used in MB.
        free_mb (float): Amount of free disk space remaining in MB.
    """

    total_mb: float = Field(
        ...,
        example=233752.44,
        description="Total disk space available in MB.",
        alias="totalMB",
    )
    used_mb: float = Field(
        ...,
        example=8530.66,
        description="Amount of disk space used in MB.",
        alias="usedMB",
    )
    free_mb: float = Field(
        ...,
        example=32670.01,
        description="Amount of free disk space remaining in MB.",
        alias="freeMB",
    )


class SystemResources(BaseAPISchema):
    """Represents system resource usage.

    Attributes:
        cpu_usage_percent (float): Percentage of CPU usage.
        memory_usage_mb (float): Amount of memory usage in MB.
        disk_usage (DiskUsage): Disk usage information.
    """

    cpu_usage_percent: float = Field(
        ...,
        example=53.9,
        description="Percentage of CPU usage.",
        alias="cpuUsagePercent",
    )
    memory_usage_mb: float = Field(
        ...,
        example=21.92,
        description="Amount of memory usage in MB.",
        alias="memoryUsageMB",
    )
    disk_usage: DiskUsage = Field(
        ...,
        description="Disk usage information.",
        alias="diskUsage",
    )


class HealthStatus(BaseAPISchema):
    """Represents the health status of the system.

    Attributes:
        status (str): Overall health status.
        uptime_seconds (float): Time the application or system has been running in seconds.
        system_resources (SystemResources): System resource usage.
        application_version (str): Version of the application.
    """

    status: str = Field(
        ...,
        example="OK",
        description="Overall health status.",
        alias="status",
    )
    uptime_seconds: float = Field(
        ...,
        example=2.57,
        description="Time the application or system has been running in seconds.",
        alias="uptimeSeconds",
    )
    system_resources: SystemResources = Field(
        ...,
        description="System resource usage.",
        alias="systemResources",
    )

    application_version: str = Field(
        ...,
        example="1.0.0",
        description="Version of the application.",
        alias="applicationVersion",
    )