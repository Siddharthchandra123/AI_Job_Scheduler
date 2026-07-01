import random

from simulator.entities.partition import Partition

from simulator.generators.base_generator import BaseGenerator


PARTITIONS = [

    "gpu-h100",

    "gpu-a100",

    "research",

    "production",

    "debug",

    "interactive",

]


class PartitionGenerator(BaseGenerator):

    def generate(self):

        return Partition(

            name=random.choice(PARTITIONS),

            gpu_type=random.choice(
                [
                    "H100",
                    "A100",
                    "L40S",
                ]
            ),

            max_nodes=random.randint(10, 150),

            qos=[
                "LOW",
                "STANDARD",
                "PREMIUM",
                "CRITICAL",
            ],

        )
