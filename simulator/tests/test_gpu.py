from simulator.generators.gpu_generator import GPUGenerator

print("="*60)
print("GPU GENERATOR TEST")
print("="*60)

gpu = GPUGenerator("H100").generate()

print(gpu)

assert gpu.memory_gb == 80

assert gpu.power_watts == 700

print("\nPASSED")
