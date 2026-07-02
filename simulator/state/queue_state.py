"""
Current scheduler queue.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class QueueState:

    pending_jobs: List[str] = field(default_factory=list)

    running_jobs: List[str] = field(default_factory=list)

    completed_jobs: List[str] = field(default_factory=list)

    failed_jobs: List[str] = field(default_factory=list)

    def enqueue(self, job_id):

        self.pending_jobs.append(job_id)

    def dequeue(self):

        if not self.pending_jobs:
            return None

        return self.pending_jobs.pop(0)
