from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from simulator.events.event_types import EventType


@dataclass(order=True)
class Event:

    timestamp: datetime

    event_type: EventType

    priority: int = 0

    payload: dict = field(default_factory=dict)

    event_id: str = field(default_factory=lambda: str(uuid4()))

    processed: bool = False

    def mark_processed(self):

        self.processed = True

    def __repr__(self):

        return (
            f"<Event "
            f"{self.event_type.value} "
            f"{self.timestamp}>"
        )
