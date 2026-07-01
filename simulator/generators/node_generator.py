import random
from uuid import uuid4

from simulator.entities.node import Node

from simulator.generators.base_generator import BaseGenerator
from simulator.generators.gpu_generator import GPUGenerator


class NodeGenerator(BaseGenerator):

    def generate(self):

        gpu_type = random.choice(
            [
                "H100",
                "A100",
                "L40S",
                "V100",
            ]
        )

        gpu_count = random.choice(
            [
                2,
                4,
                8,
            ]
        )

        gpu_generator = GPUGenerator(gpu_type)

        gpus = gpu_generator.generate_many(gpu_count)

        return Node(

            node_id=str(uuid4()),

            partition="gpu",

            cpu_cores=random.choice(
                [
                    32,
                    64,
                    96,
                ]
            ),

            ram_gb=random.choice(
                [
                    256,
                    512,
                    1024,
                ]
            ),

            gpu_type=gpu_type,

            gpu_count=gpu_count,

            power_limit=random.randint(
                1500,
                5000,
            ),

            gpus=gpus,

        )
