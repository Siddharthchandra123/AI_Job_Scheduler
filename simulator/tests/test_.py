from simulator.generators.node_generator import NodeGenerator

generator = NodeGenerator()

nodes = generator.generate_many(1000)

print(len(nodes))

assert len(nodes) == 1000
