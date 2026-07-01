import heapq

from simulator.events.event import Event


class EventQueue:

    def __init__(self):

        self._queue = []

    def push(self, event: Event):

        heapq.heappush(self._queue, event)

    def pop(self):

        if not self._queue:

            return None

        return heapq.heappop(self._queue)

    def peek(self):

        if not self._queue:

            return None

        return self._queue[0]

    def clear(self):

        self._queue.clear()

    def __len__(self):

        return len(self._queue)

    def empty(self):

        return len(self._queue) == 0
