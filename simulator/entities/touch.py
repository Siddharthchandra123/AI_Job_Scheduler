"""
Enterprise AI/HPC Job Entity

Represents one scheduling request in the simulator.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional

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

    # ---------------------------------------------------
    # Identity
    # ---------------------------------------------------

    job_id: str
    job_name: str
    comment: str = ""

    # ---------------------------------------------------
    # Ownership
    # ---------------------------------------------------

    account: str = ""
    user_id: str = ""
    department: str = ""
    customer_region: str = ""

    # ---------------------------------------------------
    # AI Workload
    # ---------------------------------------------------

    workload: WorkloadType = WorkloadType.TRAINING
    framework: Framework = Framework.PYTORCH

    model_name: str = ""
    dataset_name: str = ""

    # ---------------------------------------------------
    # Scheduling
    # ---------------------------------------------------

    partition: str = "gpu"
    qos: QoS = QoS.STANDARD
    priority: JobPriority = JobPriority.NORMAL

    scheduler: SchedulerPolicy = SchedulerPolicy.FCFS

    # ---------------------------------------------------
    # Requested Resources
    # ---------------------------------------------------

    requested_nodes: int = 1
    requested_gpus: int = 1

    requested_gpu_memory_gb: float = 40

    requested_cpu_cores: int = 8

    requested_memory_gb: float = 64

    requested_storage_gb: float = 100

    requested_network_gbps: float = 10

    # ---------------------------------------------------
    # Allocated Resources
    # ---------------------------------------------------

    allocated_nodes: int = 0

    allocated_cores: int = 0

    allocated_gpu_ids: List[str] = field(default_factory=list)

    allocated_tres: Dict = field(default_factory=dict)

    cluster: str = ""

    selected_node: str = ""

    # ---------------------------------------------------
    # Timing
    # ---------------------------------------------------

    submit_time: Optional[datetime] = None

    eligible_time: Optional[datetime] = None

    start_time: Optional[datetime] = None

    end_time: Optional[datetime] = None

    execution_time_seconds: float = 0.0

    elapsed_time_seconds: float = 0.0

    wait_time_seconds: float = 0.0

    cpu_time_seconds: float = 0.0

    total_cpu_seconds: float = 0.0

    core_hours: float = 0.0

    time_to_result_seconds: float = 0.0

    timelimit_seconds: float = 0.0

    timelimit_raw: float = 0.0

    # ---------------------------------------------------
    # Memory
    # ---------------------------------------------------

    requested_memory: float = 0.0

    consumed_memory: float = 0.0

    max_rss: float = 0.0

    memory_efficiency: float = 0.0

    # ---------------------------------------------------
    # GPU Metrics
    # ---------------------------------------------------

    gpu_utilization: float = 0.0

    gpu_memory_used: float = 0.0

    gpu_temperature: float = 0.0

    gpu_power: float = 0.0

    gpu_energy: float = 0.0

    # ---------------------------------------------------
    # Cluster Snapshot
    # ---------------------------------------------------

    cluster_load: float = 0.0

    queue_length: int = 0

    available_gpus: int = 0

    available_cpu: int = 0

    available_memory: float = 0.0

    # ---------------------------------------------------
    # AI Prediction
    # ---------------------------------------------------

    predicted_runtime: float = 0.0

    predicted_wait_time: float = 0.0

    scheduler_score: float = 0.0

    reward: float = 0.0

    # ---------------------------------------------------
    # Runtime Status
    # ---------------------------------------------------

    status: JobStatus = JobStatus.SUBMITTED

    exit_code: str = "0:0"

    flags: List[str] = field(default_factory=list)

    licenses: List[str] = field(default_factory=list)

    retry_count: int = 0

    failure_reason: str = ""

    # ---------------------------------------------------
    # Power & Sustainability
    # ---------------------------------------------------

    energy_consumption_kwh: float = 0.0

    carbon_emission_kg: float = 0.0

    # ---------------------------------------------------
    # IO
    # ---------------------------------------------------

    network_io_gb: float = 0.0

    storage_io_gb: float = 0.0

    # ---------------------------------------------------
    # Audit
    # ---------------------------------------------------

    simulation_id: str = ""

    event_id: str = ""

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: datetime = field(default_factory=datetime.utcnow)

    # ---------------------------------------------------
    # Helper Methods
    # ---------------------------------------------------

    @property
    def is_running(self) -> bool:
        return self.status == JobStatus.RUNNING

    @property
    def is_completed(self) -> bool:
        return self.status == JobStatus.COMPLETED

    @property
    def is_failed(self) -> bool:
        return self.status == JobStatus.FAILED

    @property
    def resource_vector(self) -> Dict:
        """
        Returns the requested resource vector.
        """

        return {
            "cpu": self.requested_cpu_cores,
            "memory": self.requested_memory_gb,
            "gpus": self.requested_gpus,
            "gpu_memory": self.requested_gpu_memory_gb,
            "storage": self.requested_storage_gb,
        }

    def calculate_memory_efficiency(self) -> float:

        if self.requested_memory == 0:
            return 0.0

        self.memory_efficiency = (
            self.consumed_memory /
            self.requested_memory
        ) * 100

        return round(self.memory_efficiency, 2)

    def to_dict(self):

        return self.__dict__

    def __str__(self):

        return (
            f"Job("
            f"{self.job_id}, "
            f"{self.job_name}, "
            f"{self.workload.value}, "
            f"{self.status.value})"
        )
