from simulator.entities.job import Job

print("="*60)
print("JOB ENTITY TEST")
print("="*60)

job = Job(

    job_id="JOB0001",

    job_name="Llama Training"

)

print(job)

print(job.resource_vector)

assert job.job_name == "Llama Training"

assert job.status.value == "SUBMITTED"

print("\nPASSED")
