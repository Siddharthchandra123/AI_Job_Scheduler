from simulator.config.loader import config

print("=" * 50)

print("Simulation Config")

print("=" * 50)

print(config)

assert config["simulation"]["total_jobs"] > 0

assert config["clusters"]["count"] > 0

print("\nConfiguration Loaded Successfully")
