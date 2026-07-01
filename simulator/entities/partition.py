from dataclasses import dataclass

@dataclass
class Partition:

    name: str

    gpu_type: str

    max_nodes: int

    qos: list
