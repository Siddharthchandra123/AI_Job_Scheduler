"""
AI Cloud Scheduler
Enterprise Simulation Engine
"""

from datetime import datetime

from simulator.engine.simulation_context import SimulationContext
from simulator.engine.dispatcher import Dispatcher

from simulator.events.event import Event
from simulator.events.event_types import EventType

from simulator.handlers.job_handlers import JobHandlers

from simulator.builders.cluster_state_builder import ClusterStateBuilder

from simulator.generators.cluster_generator import ClusterGenerator

from simulator.engine.resource_manager import ResourceManager

from scheduler.fcfs_scheduler import FCFSScheduler
from scheduler.scheduler_manager import SchedulerManager


class SimulationEngine:

    def __init__(self):

        print("\nInitializing Simulation Engine...")

        # --------------------------------------------------
        # Global Context
        # --------------------------------------------------

        self.context = SimulationContext()

        # --------------------------------------------------
        # Dispatcher
        # --------------------------------------------------

        self.dispatcher = Dispatcher()

        # --------------------------------------------------
        # Infrastructure
        # --------------------------------------------------

        self.cluster = ClusterGenerator().generate()

        self.cluster_state = ClusterStateBuilder.build(
            self.cluster
        )

        # --------------------------------------------------
        # Resource Manager
        # --------------------------------------------------

        self.resource_manager = ResourceManager(
            self.cluster_state
        )

        # --------------------------------------------------
        # Scheduler
        # --------------------------------------------------

        self.scheduler = FCFSScheduler(

            queue=self.context.job_queue,

            resource_manager=self.resource_manager

        )

        self.scheduler_manager = SchedulerManager(

            scheduler=self.scheduler

        )

        # --------------------------------------------------
        # Handlers
        # --------------------------------------------------

        self.handlers = JobHandlers(

    context=self.context,

    scheduler=self.scheduler_manager,

    resource_manager=self.resource_manager,

)

        

        # --------------------------------------------------
        # Register Events
        # --------------------------------------------------

        self._register_events()

        print("Simulation Engine Ready.")

    # ======================================================
    # Register Dispatcher Events
    # ======================================================

    def _register_events(self):

        self.dispatcher.register(

            EventType.JOB_SUBMITTED,

            self.handlers.handle_job_submitted

        )

        self.dispatcher.register(

            EventType.SCHEDULER_TICK,

            self.handlers.handle_scheduler_tick

        )

        self.dispatcher.register(

            EventType.JOB_STARTED,

            self.handlers.handle_job_started

        )

        self.dispatcher.register(

            EventType.JOB_COMPLETED,

            self.handlers.handle_job_completed

        )

    # ======================================================
    # Submit Event
    # ======================================================

    def submit_event(self, event: Event):

        self.context.event_queue.push(event)

    # ======================================================
    # Process One Event
    # ======================================================

    def process_next_event(self):

        queue = self.context.event_queue

        if queue.empty():

            return False

        event = queue.pop()

        self.context.clock.set_time(

            event.timestamp

        )

        self.dispatcher.dispatch(event)

        return True

    # ======================================================
    # Main Loop
    # ======================================================

    def run(self):

        print("\nStarting Simulation...\n")

        while self.process_next_event():

            pass

        print("\nSimulation Completed.\n")

    # ======================================================
    # Reset
    # ======================================================

    def reset(self):

        self.context.event_queue.clear()

    # ======================================================
    # Statistics
    # ======================================================

    def statistics(self):

        return {

            "clock": self.context.clock.now(),

            "events_remaining":

                len(self.context.event_queue),

            "jobs_waiting":

                self.context.job_queue.size(),

            "cluster":

                self.cluster.cluster_id,

            "available_gpu":

                self.cluster_state.total_available_gpu,

            "available_cpu":

                self.cluster_state.total_available_cpu

        }

    # ======================================================
    # Summary
    # ======================================================

    def summary(self):

        print()

        print("=" * 60)

        print("Simulation Summary")

        print("=" * 60)

        for key, value in self.statistics().items():

            print(f"{key:20} : {value}")

        print("=" * 60)
