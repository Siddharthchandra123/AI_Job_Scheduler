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
