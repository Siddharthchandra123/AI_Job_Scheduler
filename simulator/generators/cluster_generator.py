import random
from uuid import uuid4

from simulator.entities.cluster import Cluster

from simulator.generators.base_generator import BaseGenerator
from simulator.generators.node_generator import NodeGenerator
from simulator.generators.partition_generator import (
    PartitionGenerator,
)


class ClusterGenerator(BaseGenerator):

    def generate(self):

        node_count = random.randint(
            20,
            100,
        )

        nodes = NodeGenerator().generate_many(node_count)

        partitions = PartitionGenerator().generate_many(
            random.randint(4, 10)
        )

        return Cluster(

            cluster_id=str(uuid4()),

            region=random.choice(
                [
                    "US-East",
                    "Europe",
                    "India",
                    "Japan",
                ]
            ),

            total_nodes=node_count,

            partitions=partitions,

            nodes=nodes,

        )
