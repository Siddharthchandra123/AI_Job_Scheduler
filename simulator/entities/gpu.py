from dataclasses import dataclass

@dataclass
class GPU:

    gpu_id: str

    gpu_type: str

    memory_gb: int

    power_watts: int

    tensor_tflops: float

    status: str = "FREE"
