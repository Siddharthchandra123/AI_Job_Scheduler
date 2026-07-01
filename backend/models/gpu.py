from dataclasses import dataclass

@dataclass
class GPU:
    id: int
    memory_gb: int
    utilization: float = 0.0
    temperature: float = 35.0
    power_watts: float = 80.0
    status: str = "FREE"

    def is_available(self):
        return self.status == "FREE"
