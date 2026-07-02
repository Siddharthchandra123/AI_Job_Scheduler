from dataclasses import dataclass, field
from datetime import datetime
from itertools import count
from uuid import uuid4
from simulator.events.event_types import EventType

_counter = count()


@dataclass(order=True)
class Event:

    # Used for heap ordering
    timestamp: datetime

    # Required field
    event_type: EventType = field(compare=False)

    # Tie-breaker for same timestamp
    sequence: int = field(
        default_factory=lambda: next(_counter)
    )

    # Event data
    payload: dict = field(
        default_factory=dict,
        compare=False
    )

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


