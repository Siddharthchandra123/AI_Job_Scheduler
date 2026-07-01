import random
from uuid import uuid4

from simulator.entities.user import User
from simulator.generators.base_generator import BaseGenerator


ROLES = [
    "Research Scientist",
    "ML Engineer",
    "Platform Engineer",
    "Data Scientist",
    "Intern",
]

GPUS = [
    "H100",
    "H200",
    "A100",
    "L40S",
    "V100",
]

PRIORITY = [
    "LOW",
    "STANDARD",
    "PREMIUM",
    "CRITICAL",
]


class UserGenerator(BaseGenerator):

    def __init__(self, account_id: str):

        super().__init__()

        self.account_id = account_id

    def generate(self):

        return User(

            user_id=str(uuid4()),

            account_id=self.account_id,

            username=f"user_{random.randint(1000,9999)}",

            role=random.choice(ROLES),

            department=random.choice(
                [
                    "Research",
                    "Finance",
                    "Retail",
                    "Healthcare",
                    "Platform",
                ]
            ),

            preferred_gpu=random.choice(GPUS),

            average_jobs_per_day=random.randint(2, 30),

            average_runtime_minutes=random.randint(5, 720),

            priority_bias=random.choice(PRIORITY),

        )
