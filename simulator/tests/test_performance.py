from simulator.generators.cluster_generator import ClusterGenerator
import time

print("="*80)
print("PERFORMANCE TEST")
print("="*80)

start=time.time()

clusters=ClusterGenerator().generate_many(100)

end=time.time()

print()

print("Clusters :",len(clusters))

print("Time :",round(end-start,2),"seconds")
