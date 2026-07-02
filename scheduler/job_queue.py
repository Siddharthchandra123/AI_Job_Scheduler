"""
Enterprise Job Queue

Supports:
- FCFS
- Priority
- QoS
- Future RL Queue
"""

from collections import deque
from simulator.entities.job import Job


class JobQueue:

    def __init__(self):

        self.queue = deque()

    def enqueue(self, job: Job):

        self.queue.append(job)

    def dequeue(self):

        if self.empty():
            return None

        return self.queue.popleft()

    def peek(self):

        if self.empty():
            return None

        return self.queue[0]

    def remove(self, job_id):

        for job in self.queue:

            if job.job_id == job_id:

                self.queue.remove(job)

                return True

        return False

    def clear(self):

        self.queue.clear()

    def size(self):

        return len(self.queue)

    def empty(self):

        return len(self.queue) == 0

    def all_jobs(self):

        return list(self.queue)

    def __len__(self):

        return len(self.queue)

    def __iter__(self):

        return iter(self.queue)
