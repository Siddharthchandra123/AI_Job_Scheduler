from simulator.generators.account_generator import AccountGenerator
from simulator.generators.user_generator import UserGenerator
from simulator.generators.cluster_generator import ClusterGenerator

print("="*80)
print("AI CLOUD SCHEDULER FOUNDATION TEST")
print("="*80)

account = AccountGenerator().generate()

print()

print("ACCOUNT")

print(account)

print()

user = UserGenerator(account.account_id).generate()

print("USER")

print(user)

print()

cluster = ClusterGenerator().generate()

print("CLUSTER")

print(cluster)

print()

print("Nodes :",len(cluster.nodes))

gpu_count = 0

for node in cluster.nodes:

    gpu_count += len(node.gpus)

print("Total GPUs :",gpu_count)

print()

print("="*80)

print("FOUNDATION PIPELINE PASSED")

print("="*80)
