from dataclasses import dataclass, field
from typing import List
from .gpu import GPU


@dataclass
class Node:
    id: int
    cpu_cores: int
    ram_gb: int
    gpus: List[GPU] = field(default_factory=list)
    status: str = "HEALTHY"

    def available_gpus(self):
        return [gpu for gpu in self.gpus if gpu.is_available()]

    def utilization(self):
        busy = len(self.gpus) - len(self.available_gpus())
        return busy / len(self.gpus)
