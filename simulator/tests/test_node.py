from simulator.generators.node_generator import NodeGenerator

print("="*60)
print("NODE TEST")
print("="*60)

node = NodeGenerator().generate()

print(node)

print("GPUs :",len(node.gpus))

assert len(node.gpus) > 0

print("\nPASSED")
