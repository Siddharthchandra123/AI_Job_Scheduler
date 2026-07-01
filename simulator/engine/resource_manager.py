"""
Keeps track of cluster resources.
"""

from simulator.entities.cluster import Cluster


class ResourceManager:

    def __init__(self):

        self.clusters: list[Cluster] = []

    def add_cluster(self, cluster: Cluster):

        self.clusters.append(cluster)

    def total_nodes(self):

        return sum(len(c.nodes) for c in self.clusters)

    def total_gpus(self):

        total = 0

        for cluster in self.clusters:

            for node in cluster.nodes:

                total += node.gpu_count

        return total

    def available_nodes(self):

        available = []

        for cluster in self.clusters:

            for node in cluster.nodes:

                if node.state == "IDLE":

                    available.append(node)

        return available

    def summary(self):

        return {

            "clusters": len(self.clusters),

            "nodes": self.total_nodes(),

            "gpus": self.total_gpus(),

            "idle_nodes": len(self.available_nodes())

        }
