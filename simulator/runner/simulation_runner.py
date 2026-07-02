"""
Simulation Runner

Creates and executes complete simulations.
"""

from datetime import timedelta

from simulator.builders.simulation_builder import SimulationBuilder

from simulator.events.event_factory import EventFactory
from simulator.events.event_types import EventType

from simulator.generators.job_generator import JobGenerator


class SimulationRunner:

    def __init__(

        self,

        jobs=100,

        clusters=1,

        users=50,

        accounts=10,

    ):

        self.jobs = jobs

        self.clusters = clusters

        self.users = users

        self.accounts = accounts

    # ----------------------------------------------------

    def build_engine(self):

        self.engine = (

            SimulationBuilder()

            .with_clusters(self.clusters)

            .with_accounts(self.accounts)

            .with_users(self.users)

            .build()

        )

    # ----------------------------------------------------

    def generate_jobs(self):

        generator = JobGenerator()

        clock = self.engine.context.clock

        for i in range(self.jobs):

            job = generator.generate()

            self.engine.context.registry.add_job(job)

            submit_time = clock.now() + timedelta(seconds=i)

            self.engine.submit_event(

                EventFactory.create(
    event_type=EventType.JOB_SUBMITTED,
    timestamp=submit_time,
    payload={
        "job": job
    }
)

            )

            self.engine.submit_event(

                EventFactory.create(

                    EventType.SCHEDULER_TICK,

                    submit_time + timedelta(milliseconds=100)

                )

            )

    # ----------------------------------------------------

    def run(self):

        self.build_engine()

        self.generate_jobs()

        self.engine.run()

        self.engine.summary()
