"""
Main simulation loop.
"""

from simulator.engine.simulation_context import SimulationContext
from simulator.engine.dispatcher import Dispatcher


class SimulationEngine:

    def __init__(self):

        self.context = SimulationContext()

        self.dispatcher = Dispatcher()

    def run(self):

        queue = self.context.event_queue

        while not queue.empty():

            event = queue.pop()

            self.context.clock.set_time(

                event.timestamp

            )

            self.dispatcher.dispatch(event)
