"""
Runtime state of a compute node.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class NodeState:

    node_id: str

    # Physical Capacity
    total_cpu: int
    total_ram: int
    total_gpu: int

    # Current Usage
    allocated_cpu: int = 0
    allocated_ram: int = 0
    allocated_gpu: int = 0

    # Running Jobs
    running_jobs: List[str] = field(default_factory=list)

    state: str = "IDLE"

    @property
    def available_cpu(self):
        return self.total_cpu - self.allocated_cpu

    @property
    def available_ram(self):
        return self.total_ram - self.allocated_ram

    @property
    def available_gpu(self):
        return self.total_gpu - self.allocated_gpu

    @property
    def utilization(self):

        if self.total_gpu == 0:
            return 0

        return round(
            self.allocated_gpu / self.total_gpu,
            2
        )

    def can_allocate(
        self,
        cpu,
        ram,
        gpu
    ):

        return (
            self.available_cpu >= cpu
            and
            self.available_ram >= ram
            and
            self.available_gpu >= gpu
        )
