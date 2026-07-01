from dataclasses import dataclass

@dataclass
class User:
    user_id: str
    account_id: str
    username: str
    role: str
    department: str

    preferred_gpu: str

    average_jobs_per_day: int

    average_runtime_minutes: int

    priority_bias: str
