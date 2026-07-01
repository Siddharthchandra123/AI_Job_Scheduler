from simulator.generators.cluster_generator import ClusterGenerator

print("="*60)
print("CLUSTER TEST")
print("="*60)

cluster = ClusterGenerator().generate()

print(cluster)

print()

print("Nodes :",len(cluster.nodes))

print("Partitions :",len(cluster.partitions))

assert len(cluster.nodes) > 0

print("\nPASSED")
