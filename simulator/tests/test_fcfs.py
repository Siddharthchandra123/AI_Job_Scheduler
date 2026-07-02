from scheduler.job_queue import JobQueue
from scheduler.fcfs_scheduler import FCFSScheduler

from simulator.engine.resource_manager import ResourceManager
from simulator.state.node_state import NodeState
from simulator.state.cluster_state import ClusterState

from simulator.entities.job import Job

node = NodeState(

    node_id="NODE001",

    total_cpu=96,

    total_ram=512,

    total_gpu=8

)

cluster = ClusterState(

    cluster_id="CLUSTER"

)

cluster.nodes[node.node_id] = node

resource_manager = ResourceManager(cluster)

queue = JobQueue()

scheduler = FCFSScheduler(

    queue,

    resource_manager

)

for i in range(3):

    queue.enqueue(

        Job(

            job_id=f"JOB{i}",

            job_name="Training",

            requested_cpu_cores=8,

            requested_memory_gb=32,

            requested_gpus=2

        )

    )

while not queue.empty():

    job = scheduler.schedule()

    print(job)

print()

print(node)
