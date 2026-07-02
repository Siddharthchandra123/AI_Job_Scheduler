"""
Enterprise Resource Manager

Responsible for allocating and releasing
cluster resources.
"""

from platform import node

from simulator.state.cluster_state import ClusterState
from simulator.entities.job import Job


class ResourceManager:

    def __init__(self, cluster_state: ClusterState):

        self.cluster_state = cluster_state

    # ----------------------------------------------------
    # Find Suitable Node
    # ----------------------------------------------------

    def find_node(self, job):

        print(f"\nSearching node for {job.job_id}")

        print(
            f"Needs CPU={job.requested_cpu_cores}, "
            f"RAM={job.requested_memory_gb}, "
            f"GPU={job.requested_gpus}, "
            f"Partition={job.partition}"
        )

        for node in self.cluster_state.nodes.values():

            print(
                f"Node {node.node_id}: "
                f"CPU={node.available_cpu}, "
                f"RAM={node.available_ram}, "
                f"GPU={node.available_gpu}"
            )

            if (
                node.available_cpu >= job.requested_cpu_cores
                and node.available_ram >= job.requested_memory_gb
                and node.available_gpu >= job.requested_gpus
            ):
                return node

        return None

    # ----------------------------------------------------
    # Allocate Resources
    # ----------------------------------------------------

    def allocate(self, job: Job):

        node = self.find_node(job)

        if node is None:
            return False

        node.allocated_cpu += job.requested_cpu_cores

        node.allocated_ram += job.requested_memory_gb

        node.allocated_gpu += job.requested_gpus

        node.running_jobs.append(job.job_id)

        if node.available_gpu == 0:
            node.state = "BUSY"
        else:
            node.state = "ALLOCATED"

        job.selected_node = node.node_id

        return True

    # ----------------------------------------------------
    # Release Resources
    # ----------------------------------------------------

    def release(self, job: Job):

        node = self.cluster_state.nodes.get(job.selected_node)

        if node is None:
            return

        node.allocated_cpu -= job.requested_cpu_cores

        node.allocated_ram -= job.requested_memory_gb

        node.allocated_gpu -= job.requested_gpus

        if job.job_id in node.running_jobs:
            node.running_jobs.remove(job.job_id)

        if node.allocated_gpu == 0:
            node.state = "IDLE"

    # ----------------------------------------------------
    # Cluster Summary
    # ----------------------------------------------------

    def summary(self):

        return {

            "available_gpu": self.cluster_state.total_available_gpu,

            "available_cpu": self.cluster_state.total_available_cpu,

            "running_jobs": self.cluster_state.running_jobs,

            "queued_jobs": self.cluster_state.queued_jobs,

        }
