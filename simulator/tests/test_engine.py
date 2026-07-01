from datetime import timedelta

from simulator.engine.simulation_engine import SimulationEngine
from simulator.events.event_factory import EventFactory
from simulator.events.event_types import EventType


engine = SimulationEngine()

queue = engine.context.event_queue

clock = engine.context.clock

queue.push(

    EventFactory.create(

        EventType.SIMULATION_START,

        clock.now()

    )

)

queue.push(

    EventFactory.create(

        EventType.SCHEDULER_TICK,

        clock.now() + timedelta(seconds=5)

    )

)

queue.push(

    EventFactory.create(

        EventType.SIMULATION_END,

        clock.now() + timedelta(seconds=20)

    )

)


engine.dispatcher.register(

    EventType.SIMULATION_START,

    lambda e: print("Simulation Started")

)

engine.dispatcher.register(

    EventType.SCHEDULER_TICK,

    lambda e: print("Scheduler Tick")

)

engine.dispatcher.register(

    EventType.SIMULATION_END,

    lambda e: print("Simulation Finished")

)


engine.run()
