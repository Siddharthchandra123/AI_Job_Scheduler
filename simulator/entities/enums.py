"""
Common enums used across the AI Cloud Scheduler simulator.
"""

from enum import Enum


class JobStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    VALIDATED = "VALIDATED"
    QUEUED = "QUEUED"
    ELIGIBLE = "ELIGIBLE"
    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    TIMEOUT = "TIMEOUT"
    PREEMPTED = "PREEMPTED"


class QoS(str, Enum):
    LOW = "LOW"
    STANDARD = "STANDARD"
    PREMIUM = "PREMIUM"
    CRITICAL = "CRITICAL"


class JobPriority(str, Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class GPUState(str, Enum):
    FREE = "FREE"
    RESERVED = "RESERVED"
    BUSY = "BUSY"
    FAILED = "FAILED"
    MAINTENANCE = "MAINTENANCE"


class NodeState(str, Enum):
    IDLE = "IDLE"
    ALLOCATED = "ALLOCATED"
    BUSY = "BUSY"
    DRAINING = "DRAINING"
    DOWN = "DOWN"
    MAINTENANCE = "MAINTENANCE"


class ClusterState(str, Enum):
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    MAINTENANCE = "MAINTENANCE"
    OFFLINE = "OFFLINE"


class WorkloadType(str, Enum):
    TRAINING = "TRAINING"
    FINETUNING = "FINETUNING"
    INFERENCE = "INFERENCE"
    EMBEDDING = "EMBEDDING"
    PREPROCESSING = "PREPROCESSING"
    EVALUATION = "EVALUATION"
    HYPERPARAMETER_SEARCH = "HYPERPARAMETER_SEARCH"


class SchedulerPolicy(str, Enum):
    FCFS = "FCFS"
    ROUND_ROBIN = "ROUND_ROBIN"
    LEAST_LOADED = "LEAST_LOADED"
    PRIORITY = "PRIORITY"
    BEST_FIT = "BEST_FIT"
    AI = "AI"
    RL = "RL"


class Region(str, Enum):
    US_EAST = "US-East"
    US_WEST = "US-West"
    EUROPE = "Europe"
    INDIA = "India"
    JAPAN = "Japan"
    SINGAPORE = "Singapore"


class Framework(str, Enum):
    PYTORCH = "PyTorch"
    TENSORFLOW = "TensorFlow"
    JAX = "JAX"
    SCIKIT = "Scikit-Learn"
    XGBOOST = "XGBoost"
