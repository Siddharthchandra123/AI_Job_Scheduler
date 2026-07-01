"""
Enterprise Job Entity

Represents a single AI/HPC scheduling request.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Dict, Optional

from simulator.entities.enums import (
    JobStatus,
    QoS,
    JobPriority,
    SchedulerPolicy,
    WorkloadType,
    Framework,
)


@dataclass
class Job:

    # ============================================================
    # Identity
    # ============================================================

    job_id: str
    job_name: str
    comment: str = ""

    # ============================================================
    # Ownership
    # ============================================================

    account: str = ""
    user_id: str = ""
    department: str = ""
    customer_region: str = ""
    project: str = ""
    cost_center: str = ""

    # ============================================================
    # AI Workload
    # ============================================================

    workload: WorkloadType = WorkloadType.TRAINING
    framework: Framework = Framework.PYTORCH

    model_name: str = ""
    dataset_name: str = ""

    # ============================================================
    # Scheduling
    # ============================================================

    partition: str = "gpu"

    qos: QoS = QoS.STANDARD

    priority: JobPriority = JobPriority.NORMAL

    scheduler: SchedulerPolicy = SchedulerPolicy.FCFS

    submit_time: Optional[datetime] = None
    eligible_time: Optional[datetime] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    deadline: Optional[datetime] = None

    queue_position: int = 0

    # ============================================================
    # Requested Resources
    # ============================================================

    requested_nodes: int = 1

    requested_gpus: int = 1

    requested_cpu_cores: int = 8

    requested_memory_gb: float = 64.0

    requested_gpu_memory_gb: float = 80.0

    requested_storage_gb: float = 100.0

    requested_network_gbps: float = 10.0

    # ============================================================
    # Allocated Resources
    # ============================================================

    allocated_nodes: int = 0

    allocated_cores: int = 0

    allocated_gpu_ids: List[str] = field(default_factory=list)

    allocated_tres: Dict[str, str] = field(default_factory=dict)

    cluster: str = ""

    selected_node: str = ""

    # ============================================================
    # Runtime Metrics
    # ============================================================

    execution_time_seconds: float = 0.0

    elapsed_time_seconds: float = 0.0

    wait_time_seconds: float = 0.0

    cpu_time_seconds: float = 0.0

    total_cpu_seconds: float = 0.0

    core_hours: float = 0.0

    time_to_result_seconds: float = 0.0

    timelimit_seconds: float = 0.0

    timelimit_raw: float = 0.0

    # ============================================================
    # Memory Metrics
    # ============================================================

    requested_memory: float = 64.0

    consumed_memory: float = 0.0

    max_rss: float = 0.0

    # ============================================================
    # GPU Metrics
    # ============================================================

    gpu_utilization: float = 0.0

    gpu_memory_used: float = 0.0

    gpu_temperature: float = 0.0

    gpu_power: float = 0.0

    gpu_energy: float = 0.0

    # ============================================================
    # Cluster Snapshot
    # ============================================================

    cluster_load: float = 0.0

    queue_length: int = 0

    available_gpus: int = 0

    available_cpu: int = 0

    available_memory: float = 0.0

    # ============================================================
    # AI Prediction
    # ============================================================

    predicted_runtime: float = 0.0

    predicted_wait_time: float = 0.0

    scheduler_score: float = 0.0

    reward: float = 0.0

    # ============================================================
    # Status
    # ============================================================

    status: JobStatus = JobStatus.SUBMITTED

    exit_code: str = "0:0"

    flags: List[str] = field(default_factory=list)

    licenses: List[str] = field(default_factory=list)

    retry_count: int = 0

    failure_reason: str = ""

    # ============================================================
    # Sustainability
    # ============================================================

    energy_consumption_kwh: float = 0.0

    carbon_emission_kg: float = 0.0

    # ============================================================
    # IO Metrics
    # ============================================================

    network_io_gb: float = 0.0

    storage_io_gb: float = 0.0

    # ============================================================
    # Audit
    # ============================================================

    simulation_id: str = ""

    event_id: str = ""

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # ============================================================
    # Helper Properties
    # ============================================================

    @property
    def is_running(self):
        return self.status == JobStatus.RUNNING

    @property
    def is_completed(self):
        return self.status == JobStatus.COMPLETED

    @property
    def is_failed(self):
        return self.status == JobStatus.FAILED

    @property
    def runtime_hours(self):
        return round(self.execution_time_seconds / 3600, 2)

    @property
    def memory_efficiency(self):

        if self.requested_memory == 0:
            return 0.0

        return round(
            (self.consumed_memory / self.requested_memory) * 100,
            2,
        )

    @property
    def resource_vector(self):

        return {

            "nodes": self.requested_nodes,

            "cpu": self.requested_cpu_cores,

            "memory": self.requested_memory_gb,

            "gpus": self.requested_gpus,

            "gpu_memory": self.requested_gpu_memory_gb,

            "storage": self.requested_storage_gb,

            "network": self.requested_network_gbps,
        }

    @property
    def utilization(self):

        if self.requested_gpus == 0:
            return 0.0

        return round(self.gpu_utilization, 2)

    # ============================================================
    # Helper Methods
    # ============================================================

    def allocate(
        self,
        cluster: str,
        node: str,
        gpu_ids: List[str],
    ):

        self.cluster = cluster
        self.selected_node = node
        self.allocated_gpu_ids = gpu_ids
        self.status = JobStatus.SCHEDULED

    def start(self):

        self.start_time = datetime.utcnow()
        self.status = JobStatus.RUNNING

    def complete(self):

        self.end_time = datetime.utcnow()
        self.status = JobStatus.COMPLETED

        if self.start_time:

            self.execution_time_seconds = (
                self.end_time - self.start_time
            ).total_seconds()

    def fail(self, reason: str):

        self.failure_reason = reason
        self.status = JobStatus.FAILED

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        return cls(**data)

    def __repr__(self):

        return (
            f"Job("
            f"id={self.job_id}, "
            f"name={self.job_name}, "
            f"status={self.status.value}, "
            f"gpu={self.requested_gpus}, "
            f"cpu={self.requested_cpu_cores})"
        )
