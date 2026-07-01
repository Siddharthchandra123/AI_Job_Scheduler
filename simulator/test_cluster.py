from simulator.cluster_generator import create_cluster

cluster = create_cluster(5)

print("=" * 60)

print("AI CLOUD CLUSTER")

print("=" * 60)

for node in cluster.nodes:

    print()

    print(f"Node {node.id}")

    print(f"CPU : {node.cpu_cores}")

    print(f"RAM : {node.ram_gb} GB")

    print(f"GPUs : {len(node.gpus)}")

    print(f"Available : {len(node.available_gpus())}")

    for gpu in node.gpus:

        print(
            f"   GPU {gpu.id} | {gpu.memory_gb} GB | {gpu.status}"
        )

print()

print("Total GPUs :", cluster.total_gpus())

print("Free GPUs :", cluster.free_gpus())
