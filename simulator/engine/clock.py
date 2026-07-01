"""
Virtual simulation clock.
"""

from datetime import datetime, timedelta


class SimulationClock:

    def __init__(self, start_time: datetime | None = None):

        self.current_time = start_time or datetime.utcnow()

    def now(self):

        return self.current_time

    def advance(self, seconds: float):

        self.current_time += timedelta(seconds=seconds)

    def set_time(self, timestamp: datetime):

        self.current_time = timestamp

    def reset(self, timestamp: datetime):

        self.current_time = timestamp

    def __repr__(self):

        return f"SimulationClock({self.current_time})"
