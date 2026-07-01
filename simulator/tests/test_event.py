from datetime import datetime, timedelta

from simulator.events.event_factory import EventFactory
from simulator.events.event_queue import EventQueue
from simulator.events.event_types import EventType


queue = EventQueue()

queue.push(

    EventFactory.create(

        EventType.JOB_SUBMITTED,

        datetime.now()+timedelta(seconds=20),

        job="JOB001"

    )

)

queue.push(

    EventFactory.create(

        EventType.JOB_COMPLETED,

        datetime.now()+timedelta(seconds=80),

        job="JOB002"

    )

)

queue.push(

    EventFactory.create(

        EventType.SCHEDULER_TICK,

        datetime.now()+timedelta(seconds=5)

    )

)

while not queue.empty():

    print(queue.pop())
