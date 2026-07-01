from dataclasses import dataclass, field
from typing import List
from .node import Node


@dataclass
class Cluster:
    nodes: List[Node] = field(default_factory=list)

    def total_gpus(self):
        return sum(len(node.gpus) for node in self.nodes)

    def free_gpus(self):
        total = 0

        for node in self.nodes:
            total += len(node.available_gpus())

        return total
