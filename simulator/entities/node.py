from dataclasses import dataclass, field
from typing import List

from simulator.entities.gpu import GPU


@dataclass
class Node:

    node_id: str

    partition: str

    cpu_cores: int

    ram_gb: int

    gpu_type: str

    gpu_count: int

    power_limit: int

    gpus: List[GPU] = field(default_factory=list)

    state: str = "IDLE"

    def __post_init__(self):
        self.available_cpu = self.cpu_cores
        self.available_ram_gb = self.ram_gb
        self.available_gpus = self.gpu_count
        
    def can_allocate(self, job):

        return (
            self.available_cpu >= job.requested_cpu_cores
            and self.available_ram_gb >= job.requested_memory_gb
            and self.available_gpus >= job.requested_gpus
            and self.partition == job.partition
        )