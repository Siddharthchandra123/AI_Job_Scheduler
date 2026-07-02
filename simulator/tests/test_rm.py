from simulator.entities.job import Job

from simulator.state.node_state import NodeState
from simulator.state.cluster_state import ClusterState

from simulator.engine.resource_manager import ResourceManager


# ----------------------------------------
# Build Cluster
# ----------------------------------------

node = NodeState(

    node_id="NODE001",

    total_cpu=96,

    total_ram=512,

    total_gpu=8

)

cluster = ClusterState(

    cluster_id="CLUSTER001"

)

cluster.nodes[node.node_id] = node

manager = ResourceManager(cluster)

# ----------------------------------------
# Create Job
# ----------------------------------------

job = Job(

    job_id="JOB001",

    job_name="Llama Training",

    requested_cpu_cores=16,

    requested_memory_gb=64,

    requested_gpus=2,

)

print()

print("Before Allocation")

print(node)

print()

allocated = manager.allocate(job)

print("Allocated:", allocated)

print()

print(node)

print()

manager.release(job)

print("After Release")

print(node)
