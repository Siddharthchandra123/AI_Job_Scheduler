from uuid import uuid4

from simulator.catalog.gpu_catalog import GPU_CATALOG
from simulator.entities.gpu import GPU
from simulator.generators.base_generator import BaseGenerator


class GPUGenerator(BaseGenerator):

    def __init__(self, gpu_type: str):

        super().__init__()

        self.definition = GPU_CATALOG[gpu_type]

    def generate(self):

        return GPU(

            gpu_id=str(uuid4()),

            gpu_type=self.definition["name"],

            memory_gb=self.definition["memory"],

            power_watts=self.definition["power"],

            tensor_tflops=self.definition["tensor_tflops"],

        )
