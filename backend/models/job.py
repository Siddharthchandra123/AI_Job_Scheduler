from dataclasses import dataclass
from typing import Optional

@dataclass
class Job:

    id: int

    model: str

    task: str

    user: str

    priority: str

    gpu_required: int

    cpu_required: int

    ram_required: int

    gpu_memory_required: int

    runtime_minutes: int

    dataset_size_gb: float

    batch_size: int

    arrival_time: int

    deadline: Optional[int] = None

    status: str = "QUEUED"

    assigned_node: Optional[int] = None
