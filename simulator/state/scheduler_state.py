"""
Runtime scheduler statistics.
"""

from dataclasses import dataclass


@dataclass
class SchedulerState:

    scheduler_name: str = "FCFS"

    scheduling_cycles: int = 0

    successful_allocations: int = 0

    failed_allocations: int = 0

    average_wait_time: float = 0

    average_runtime: float = 0

    gpu_utilization: float = 0

    throughput: float = 0
