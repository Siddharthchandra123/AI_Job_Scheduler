"""
Job lifecycle handlers.
"""

from datetime import timedelta

from simulator.events.event_factory import EventFactory
from simulator.events.event_types import EventType


class JobHandlers:

    def __init__(
        self,
        context,
        scheduler,
        resource_manager,
    ):

        self.context = context
        self.scheduler = scheduler
        self.resource_manager = resource_manager
    # -------------------------------------------------

    def handle_job_submitted(self, event):

        job = event.payload["job"]

        self.context.job_queue.enqueue(job)

        print(f"[{self.context.clock.now()}] Job Submitted : {job.job_id}")

        # Wake up scheduler
        self.context.event_queue.push(

            EventFactory.create(

                EventType.SCHEDULER_TICK,

                timestamp=event.timestamp + timedelta(milliseconds=1),

            )

        )
    # -------------------------------------------------

    def handle_scheduler_tick(self, event):

        print("Scheduler Tick")

        jobs = self.scheduler.run_until_blocked()

        print(f"Scheduled {len(jobs)} jobs")

        if not jobs:
            return

        for job in jobs:

            print(f"Creating START event for {job.job_id}")

            self.context.event_queue.push(
                EventFactory.create(
                    EventType.JOB_STARTED,
                    timestamp=event.timestamp + timedelta(milliseconds=100),
                    payload={"job": job},
                )
            )
    # -------------------------------------------------

    def handle_job_started(self, event):

        job = event.payload["job"]

        job.start()

        print(f"[{self.context.clock.now()}] Job Started : {job.job_id}")

        completion_time = (
            self.context.clock.now()
            + timedelta(seconds=job.execution_time_seconds)
        )

        completion_event = EventFactory.create(

            event_type=EventType.JOB_COMPLETED,

            timestamp=completion_time,

            payload={
                "job": job
            }

        )

        print("Completion Event:", completion_event)

        self.context.event_queue.push(completion_event)

    # -------------------------------------------------

    def handle_job_completed(self, event):

        job = event.payload["job"]

        print(f"[{event.timestamp}] Job Completed : {job.job_id}")

        job.complete()

        self.resource_manager.release(job)

        self.context.event_queue.push(

            EventFactory.create(

                EventType.SCHEDULER_TICK,

                timestamp=event.timestamp + timedelta(milliseconds=1),

            )

        )


