from dataclasses import dataclass

@dataclass
class Account:
    account_id: str
    organization_name: str
    industry: str
    region: str
    department_count: int
