from datetime import timedelta

from simulator.entities.job import Job

from simulator.events.event_factory import EventFactory
from simulator.events.event_types import EventType

from simulator.engine.simulation_engine import SimulationEngine


engine = SimulationEngine()

clock = engine.context.clock

for i in range(10):

    job = Job(

        job_id=f"JOB{i}",

        job_name="Llama",

        requested_cpu_cores=8,

        requested_memory_gb=32,

        requested_gpus=2,

        execution_time_seconds=30

    )

    engine.context.event_queue.push(

        EventFactory.create(

            EventType.JOB_SUBMITTED,

            clock.now() + timedelta(seconds=i),

            job=job

        )

    )

    engine.context.event_queue.push(

        EventFactory.create(

            EventType.SCHEDULER_TICK,

            clock.now() + timedelta(seconds=i + 1)

        )

    )

engine.run()
