"""
GPU Hardware Catalog
"""

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
