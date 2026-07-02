"""

import random
from datetime import datetime

from simulator.entities.job import Job

from simulator.catalog.workload_catalog import WORKLOADS
from simulator.catalog.gpu_catalog import GPU_TYPES
from simulator.catalog.organization_catalog import (
    ACCOUNTS,
    REGIONS,
    CUSTOMER_DEPARTMENTS,
    PARTITIONS,
    QOS_LEVELS,
    LICENSES,
    FLAGS,
    TIME_LIMITS,
)


class JobGenerator:

    def __init__(self):

        self.counter = 1

    # --------------------------------------------------------

    def _job_id(self):

        job_id = f"JOB-{self.counter:08d}"

        self.counter += 1

        return job_id

    # --------------------------------------------------------

    def generate(self):

        workload = random.choice(WORKLOADS)

        runtime = random.randint(
            workload.get("runtime_min", 10),
            workload.get("runtime_max", 60),
        )

        cpu = random.randint(
            workload.get("cpu_min", 4),
            workload.get("cpu_max", 16),
        )

        gpu = random.randint(
            workload.get("gpu_min", 1),
            workload.get("gpu_max", 1),
        )

        memory = random.randint(
            workload.get("memory_min", 8),
            workload.get("memory_max", 64),
        )

        qos = random.choice(QOS_LEVELS)

        return Job(

            # -------------------------------------------------
            # Identity
            # -------------------------------------------------

            job_id=self._job_id(),

            job_name=workload.get("name", "AI Job"),

            comment=workload.get(
                "description",
                "Synthetic AI workload"
            ),

            account=random.choice(ACCOUNTS),

            user_id=f"USER-{random.randint(1,100):04d}",

            # -------------------------------------------------
            # Classification
            # -------------------------------------------------

            workload_type=workload.get(
                "type",
                "training"
            ),

            partition=random.choice(PARTITIONS),

            qos=qos,

            priority=random.randint(1, 100),

            customer_region=random.choice(REGIONS),

            customer_department=random.choice(
                CUSTOMER_DEPARTMENTS
            ),

            # -------------------------------------------------
            # Resources
            # -------------------------------------------------

            requested_cpu_cores=cpu,

            requested_memory_gb=memory,

            requested_gpus=gpu,

            gpu_type=random.choice(GPU_TYPES),

            allocated_nodes=max(1, (gpu + 7) // 8),

            # -------------------------------------------------
            # Timing
            # -------------------------------------------------

            submit_time=datetime.now(),

            execution_time_seconds=runtime * 60,

            expected_runtime_minutes=runtime,

            time_limit=random.choice(TIME_LIMITS),

            # -------------------------------------------------
            # Metadata
            # -------------------------------------------------

            licenses=random.choice(LICENSES),

            flags=random.choice(FLAGS),

            retry_count=0,

            status="PENDING",

            tags=[
                workload.get("type", "training"),
                qos,
            ],
        )

    # --------------------------------------------------------

    def generate_many(self, count):

        return [

            self.generate()

            for _ in range(count)

        ]

    # --------------------------------------------------------

    def generate_stream(self):

        while True:

            yield self.generators
"""
"""
Enterprise Job Generator
"""

import random
from datetime import datetime

from simulator.entities.job import Job
from simulator.entities.enums import (
    JobStatus,
    QoS,
    JobPriority,
    SchedulerPolicy,
    WorkloadType,
    Framework,
)

from simulator.catalog.workload_catalog import WORKLOADS
from simulator.catalog.organization_catalog import (
    ACCOUNTS,
    REGIONS,
    CUSTOMER_DEPARTMENTS,
    PARTITIONS,
    LICENSES,
    FLAGS,
    MODEL_NAMES,
)

from simulator.catalog.gpu_catalog import GPU_TYPES


class JobGenerator:

    def __init__(self):

        self.counter = 1

    # -----------------------------------------------------

    def _job_id(self):

        job = f"JOB-{self.counter:08d}"

        self.counter += 1

        return job

    # -----------------------------------------------------

    def generate(self):

        workload = random.choice(WORKLOADS)

        runtime = random.randint(
            workload["runtime_min"],
            workload["runtime_max"],
        )

        cpu = random.randint(
            workload["cpu_min"],
            workload["cpu_max"],
        )

        gpu = random.randint(
            workload["gpu_min"],
            workload["gpu_max"],
        )

        memory = random.randint(
            workload["memory_min"],
            workload["memory_max"],
        )

        return Job(

            # -------------------------------------------------
            # Identity
            # -------------------------------------------------

            job_id=self._job_id(),

            job_name=workload["name"],

            comment=workload["description"],

            # -------------------------------------------------
            # Ownership
            # -------------------------------------------------

            account=random.choice(ACCOUNTS),

            user_id=f"USER-{random.randint(1,100):04d}",

            department=random.choice(CUSTOMER_DEPARTMENTS),

            customer_region=random.choice(REGIONS),

            project="AI Cloud",

            cost_center="CC-001",

            # -------------------------------------------------
            # AI
            # -------------------------------------------------

            workload=WorkloadType(
                workload["type"]
            ),

            framework=random.choice(
                [
                    Framework.PYTORCH,
                    Framework.TENSORFLOW,
                ]
            ),

            model_name=random.choice(MODEL_NAMES),

            dataset_name="Synthetic Dataset",

            # -------------------------------------------------
            # Scheduling
            # -------------------------------------------------

            partition=random.choice(PARTITIONS),

            qos=random.choice(list(QoS)),

            priority=random.choice(list(JobPriority)),

            scheduler=SchedulerPolicy.FCFS,

            submit_time=datetime.utcnow(),

            eligible_time=datetime.utcnow(),

            # -------------------------------------------------
            # Requested Resources
            # -------------------------------------------------

            requested_nodes=max(1, (gpu + 7) // 8),

            requested_gpus=gpu,

            requested_cpu_cores=cpu,

            requested_memory_gb=memory,

            requested_gpu_memory_gb=80,

            requested_storage_gb=random.randint(50, 1000),

            requested_network_gbps=random.choice(
                [10, 25, 40, 100]
            ),

            # -------------------------------------------------
            # Runtime
            # -------------------------------------------------

            execution_time_seconds=runtime * 60,

            timelimit_seconds=(runtime + 30) * 60,

            timelimit_raw=(runtime + 30) * 60,

            # -------------------------------------------------
            # Status
            # -------------------------------------------------

            status=JobStatus.SUBMITTED,

            exit_code="0:0",

            flags=[random.choice(FLAGS)],

            licenses=[random.choice(LICENSES)],

            retry_count=0,

        )

    # -----------------------------------------------------

    def generate_many(self, count):

        return [

            self.generate()

            for _ in range(count)

        ]

    # -----------------------------------------------------

    def generate_stream(self):

        while True:

            yield self.generate()
