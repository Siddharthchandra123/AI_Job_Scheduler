"""
AI Cloud Scheduler

Global Simulation Context

This object is shared by the entire simulator.

It stores every runtime object required by the
simulation engine.
"""

from simulator.engine.clock import SimulationClock
from simulator.events.event_queue import EventQueue

from simulator.core.registry import Registry

from scheduler.job_queue import JobQueue


class SimulationContext:

    def __init__(self):

        # =====================================================
        # Core Runtime
        # =====================================================

        self.clock = SimulationClock()

        self.event_queue = EventQueue()

        self.job_queue = JobQueue()

        self.registry = Registry()

        # =====================================================
        # Runtime State
        # =====================================================

        self.cluster_state = None

        self.scheduler = None

        self.resource_manager = None

        # =====================================================
        # Metrics
        # =====================================================

        self.metrics = {}

        # =====================================================
        # Statistics
        # =====================================================

        self.total_jobs = 0

        self.running_jobs = 0

        self.completed_jobs = 0

        self.failed_jobs = 0

        self.scheduler_cycles = 0

    # =========================================================

    def summary(self):

        return {

            "clock": self.clock.now(),

            "events": len(self.event_queue),

            "queue": self.job_queue.size(),

            "jobs": self.total_jobs,

            "running": self.running_jobs,

            "completed": self.completed_jobs,

            "failed": self.failed_jobs,

            "scheduler_cycles": self.scheduler_cycles,

        }

    # =========================================================

    def reset(self):

        self.event_queue.clear()

        self.job_queue.clear()

        self.metrics.clear()

        self.total_jobs = 0

        self.running_jobs = 0

        self.completed_jobs = 0

        self.failed_jobs = 0

        self.scheduler_cycles = 0
