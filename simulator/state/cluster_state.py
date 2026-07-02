"""
Runtime state of an entire cluster.
"""

from dataclasses import dataclass, field
from typing import Dict

from simulator.state.node_state import NodeState


@dataclass
class ClusterState:

    cluster_id: str

    nodes: Dict[str, NodeState] = field(default_factory=dict)

    running_jobs: int = 0

    queued_jobs: int = 0

    completed_jobs: int = 0

    failed_jobs: int = 0

    @property
    def total_available_gpu(self):

        return sum(
            node.available_gpu
            for node in self.nodes.values()
        )

    @property
    def total_available_cpu(self):

        return sum(
            node.available_cpu
            for node in self.nodes.values()
        )
