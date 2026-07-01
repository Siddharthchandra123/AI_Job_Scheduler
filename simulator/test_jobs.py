from simulator.job_generator import generate_jobs

jobs = generate_jobs(10)

print("=" * 90)

for job in jobs:
    print(job)

print("=" * 90)
