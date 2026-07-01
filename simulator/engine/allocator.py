"""
Resource allocation.
"""

from simulator.entities.job import Job
from simulator.entities.node import Node


class Allocator:

    def allocate(

        self,

        job: Job,

        node: Node,

    ):

        node.state = "BUSY"

        node.gpu_count -= job.requested_gpus

        node.cpu_cores -= job.requested_cpu_cores

        node.ram_gb -= job.requested_memory_gb

        job.selected_node = node.node_id

        return True

    def release(

        self,

        job: Job,

        node: Node,

    ):

        node.state = "IDLE"

        node.gpu_count += job.requested_gpus

        node.cpu_cores += job.requested_cpu_cores

        node.ram_gb += job.requested_memory_gb
