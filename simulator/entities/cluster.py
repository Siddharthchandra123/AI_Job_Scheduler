from dataclasses import dataclass, field
from typing import List

from simulator.entities.node import Node
from simulator.entities.partition import Partition


@dataclass
class Cluster:

    cluster_id: str

    region: str

    total_nodes: int

    partitions: List[Partition] = field(default_factory=list)

    nodes: List[Node] = field(default_factory=list)

    state: str = "ACTIVE"

    @property
    def total_gpus(self):

        return sum(node.gpu_count for node in self.nodes)

    @property
    def total_cpu(self):

        return sum(node.cpu_cores for node in self.nodes)

    @property
    def total_ram(self):

        return sum(node.ram_gb for node in self.nodes)

    def __str__(self):

        return (
            f"Cluster("
            f"{self.cluster_id}, "
            f"Nodes={len(self.nodes)}, "
            f"GPUs={self.total_gpus})"
        )
