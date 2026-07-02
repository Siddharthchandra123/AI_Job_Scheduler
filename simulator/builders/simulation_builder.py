"""
Enterprise Simulation Builder

Creates a fully configured simulation engine.
"""

from simulator.engine.simulation_engine import SimulationEngine

from simulator.generators.cluster_generator import ClusterGenerator

from simulator.generators.account_generator import AccountGenerator

from simulator.generators.user_generator import UserGenerator

from simulator.builders.cluster_state_builder import (
    ClusterStateBuilder,
)


class SimulationBuilder:

    def __init__(self):

        self.cluster_count = 1

        self.account_count = 5

        self.user_count = 50

    # =========================================================

    def with_clusters(self, count):

        self.cluster_count = count

        return self

    # =========================================================

    def with_accounts(self, count):

        self.account_count = count

        return self

    # =========================================================

    def with_users(self, count):

        self.user_count = count

        return self

    # =========================================================

    def build(self):

        engine = SimulationEngine()

        # -----------------------------------------------------
        # Create Cluster
        # -----------------------------------------------------

        cluster = ClusterGenerator().generate()

        cluster_state = ClusterStateBuilder.build(cluster)

        engine.cluster = cluster

        engine.cluster_state = cluster_state

        engine.resource_manager.cluster_state = cluster_state

        engine.context.cluster_state = cluster_state

        # -----------------------------------------------------
        # Accounts
        # -----------------------------------------------------

        account_generator = AccountGenerator()

        for _ in range(self.account_count):

            account = account_generator.generate()

            engine.context.registry.add_account(account)

        # -----------------------------------------------------
        # Users
        # -----------------------------------------------------

        user_generator = UserGenerator()

        account_ids = list(engine.context.registry.accounts.keys())

        for i in range(self.user_count):

            account_id = account_ids[i % len(account_ids)]

            user = user_generator.generate(account_id)

            engine.context.registry.add_user(user)

        return engine
