from datetime import datetime

from simulator.events.event import Event
from simulator.events.event_types import EventType


class EventFactory:

    @staticmethod
    def create(

        event_type: EventType,

        timestamp: datetime,

        **payload

    ):

        return Event(

            timestamp=timestamp,

            event_type=event_type,

            payload=payload

        )
