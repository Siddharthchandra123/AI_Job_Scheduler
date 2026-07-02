"""
GPU Hardware Catalog
"""
"""
GPU Catalog

Enterprise GPU specifications used throughout the simulator.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GPUProfile:

    name: str

    vendor: str

    architecture: str

    memory_gb: int

    cuda_cores: int

    tensor_tflops: float

    bandwidth_gbps: int

    power_watts: int

    max_temperature: int

    nvlink: bool

    generation: str


GPU_CATALOG = {

    "V100": GPUProfile(

        name="NVIDIA V100",
        vendor="NVIDIA",
        architecture="Volta",
        memory_gb=32,
        cuda_cores=5120,
        tensor_tflops=125,
        bandwidth_gbps=900,
        power_watts=300,
        max_temperature=85,
        nvlink=True,
        generation="V100",
    ),

    "A100_40GB": GPUProfile(

        name="NVIDIA A100 40GB",
        vendor="NVIDIA",
        architecture="Ampere",
        memory_gb=40,
        cuda_cores=6912,
        tensor_tflops=312,
        bandwidth_gbps=1555,
        power_watts=400,
        max_temperature=85,
        nvlink=True,
        generation="A100",
    ),

    "A100_80GB": GPUProfile(

        name="NVIDIA A100 80GB",
        vendor="NVIDIA",
        architecture="Ampere",
        memory_gb=80,
        cuda_cores=6912,
        tensor_tflops=312,
        bandwidth_gbps=2039,
        power_watts=400,
        max_temperature=85,
        nvlink=True,
        generation="A100",
    ),

    "L40S": GPUProfile(

        name="NVIDIA L40S",
        vendor="NVIDIA",
        architecture="Ada Lovelace",
        memory_gb=48,
        cuda_cores=18176,
        tensor_tflops=733,
        bandwidth_gbps=864,
        power_watts=350,
        max_temperature=88,
        nvlink=False,
        generation="L40S",
    ),

    "H100": GPUProfile(

        name="NVIDIA H100 SXM",
        vendor="NVIDIA",
        architecture="Hopper",
        memory_gb=80,
        cuda_cores=16896,
        tensor_tflops=989,
        bandwidth_gbps=3350,
        power_watts=700,
        max_temperature=90,
        nvlink=True,
        generation="H100",
    ),

    "H200": GPUProfile(

        name="NVIDIA H200",
        vendor="NVIDIA",
        architecture="Hopper",
        memory_gb=141,
        cuda_cores=16896,
        tensor_tflops=989,
        bandwidth_gbps=4800,
        power_watts=700,
        max_temperature=90,
        nvlink=True,
        generation="H200",
    ),

    "B200": GPUProfile(

        name="NVIDIA B200",
        vendor="NVIDIA",
        architecture="Blackwell",
        memory_gb=192,
        cuda_cores=24576,
        tensor_tflops=4500,
        bandwidth_gbps=8000,
        power_watts=1000,
        max_temperature=95,
        nvlink=True,
        generation="Blackwell",
    ),
}

GPU_TYPES = list(GPU_CATALOG.keys())
GPU_CATALOG = {

    "V100": {
        "name": "Tesla V100",
        "memory": 32,
        "power": 300,
        "tensor_tflops": 125,
        "cuda": "7.0",
        "hourly_cost": 2.50,
        "failure_rate": 0.002
    },

    "A100": {
        "name": "NVIDIA A100",
        "memory": 80,
        "power": 400,
        "tensor_tflops": 312,
        "cuda": "8.0",
        "hourly_cost": 4.80,
        "failure_rate": 0.0015
    },

    "H100": {
        "name": "NVIDIA H100",
        "memory": 80,
        "power": 700,
        "tensor_tflops": 989,
        "cuda": "9.0",
        "hourly_cost": 8.20,
        "failure_rate": 0.001
    },

    "H200": {
        "name": "NVIDIA H200",
        "memory": 141,
        "power": 700,
        "tensor_tflops": 1100,
        "cuda": "9.0",
        "hourly_cost": 9.30,
        "failure_rate": 0.001
    },

    "B200": {
        "name": "NVIDIA B200",
        "memory": 192,
        "power": 1000,
        "tensor_tflops": 1800,
        "cuda": "10.0",
        "hourly_cost": 15.0,
        "failure_rate": 0.0008
    },

    "L40S": {
        "name": "NVIDIA L40S",
        "memory": 48,
        "power": 350,
        "tensor_tflops": 362,
        "cuda": "8.9",
        "hourly_cost": 3.80,
        "failure_rate": 0.0018
    }

}
