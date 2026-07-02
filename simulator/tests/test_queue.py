from scheduler.job_queue import JobQueue
from simulator.entities.job import Job

queue = JobQueue()

for i in range(5):

    queue.enqueue(

        Job(

            job_id=f"JOB{i}",

            job_name=f"Training-{i}"

        )

    )

print(queue.size())

while not queue.empty():

    print(queue.dequeue())
