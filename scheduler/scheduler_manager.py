class SchedulerManager:

    def __init__(self, scheduler):

        self.scheduler = scheduler

    def run_cycle(self):

        return self.scheduler.schedule()

    def run_until_blocked(self):

        jobs = []

        while True:

            job = self.scheduler.schedule()

            if job is None:

                break

            jobs.append(job)

        return jobs

    @property
    def resource_manager(self):

        return self.scheduler.resource_manager