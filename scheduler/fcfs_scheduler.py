from scheduler.base_scheduler import BaseScheduler


class FCFSScheduler(BaseScheduler):

    def __init__(

        self,

        queue,

        resource_manager,

    ):

        self.queue = queue

        self.resource_manager = resource_manager

    def schedule(self):

        print(f"[FCFS] Queue size = {self.queue.size()}")

        if self.queue.empty():
            print("[FCFS] Queue Empty")
            return None

        job = self.queue.peek()

        print(f"[FCFS] Trying {job.job_id}")

        success = self.resource_manager.allocate(job)

        print(f"[FCFS] Allocation = {success}")

        if not success:
            return None

        self.queue.dequeue()

        print(f"[FCFS] Scheduled {job.job_id}")

        return job