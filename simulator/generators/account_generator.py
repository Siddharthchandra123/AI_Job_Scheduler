from uuid import uuid4
import random

from simulator.entities.account import Account
from simulator.catalog.organization_catalog import (
    ORGANIZATIONS,
    INDUSTRIES,
)

from simulator.catalog.region_catalog import REGIONS
from simulator.generators.base_generator import BaseGenerator


class AccountGenerator(BaseGenerator):

    def generate(self) -> Account:

        organization = random.choice(ORGANIZATIONS)

        return Account(

            account_id=str(uuid4()),

            organization_name=organization,

            industry=random.choice(INDUSTRIES),

            region=random.choice(REGIONS),

            department_count=random.randint(3, 10),

        )
