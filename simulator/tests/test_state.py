from simulator.state.node_state import NodeState

node = NodeState(

    node_id="NODE001",

    total_cpu=96,

    total_ram=512,

    total_gpu=8

)

print(node)

print()

print("Available GPU :", node.available_gpu)

print("Can Allocate 2 GPU :", node.can_allocate(

    cpu=16,

    ram=64,

    gpu=2

))
