"""
Global simulation context.

Shared across every scheduler,
allocator and event handler.
"""

from simulator.engine.clock import SimulationClock
from simulator.events.event_queue import EventQueue


class SimulationContext:

    def __init__(self):

        self.clock = SimulationClock()

        self.event_queue = EventQueue()

        # Infrastructure
        self.clusters = []

        self.accounts = []

        self.users = []

        # Jobs

        self.pending_jobs = []

        self.running_jobs = []

        self.completed_jobs = []

        self.failed_jobs = []

        # Metrics

        self.metrics = {}

        # Scheduler

        self.scheduler = None

    def summary(self):

        return {

            "clusters": len(self.clusters),

            "accounts": len(self.accounts),

            "users": len(self.users),

            "pending_jobs": len(self.pending_jobs),

            "running_jobs": len(self.running_jobs),

            "completed_jobs": len(self.completed_jobs),

            "failed_jobs": len(self.failed_jobs),

            "events": len(self.event_queue),

        }
