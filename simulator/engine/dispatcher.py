"""
Routes events.
"""

from simulator.events.event_types import EventType


class Dispatcher:

    def __init__(self):

        self.handlers = {}

    def register(

        self,

        event_type,

        handler,

    ):

        self.handlers[event_type] = handler

    def dispatch(

        self,

        event,

    ):

        handler = self.handlers.get(event.event_type)

        if handler:

            handler(event)
