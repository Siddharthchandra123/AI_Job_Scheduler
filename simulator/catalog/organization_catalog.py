"""
Organizations using the platform.
"""
"""
Organization Catalog

Enterprise organizations, regions, departments,
QoS levels, licenses, and account metadata used
for synthetic workload generation.
"""

# ============================================================
# Organizations
# ============================================================

ORGANIZATIONS = [

    "OpenAI",
    "NVIDIA",
    "Microsoft",
    "Google DeepMind",
    "Meta",
    "IBM",
    "Amazon",
    "Oracle",
    "Tesla AI",
    "Adobe",
    "Salesforce",
    "Intel",
    "AMD",
    "Samsung Research",
    "Autonomous Systems",
    "Healthcare AI",
    "Financial Analytics",
    "Cloud Platform",
    "AI Research Lab",
    "Enterprise AI",

]

# ============================================================
# Industries
# ============================================================

INDUSTRIES = [

    "Technology",
    "Finance",
    "Healthcare",
    "Manufacturing",
    "Retail",
    "Education",
    "Research",
    "Telecommunications",
    "Government",
    "Automotive",

]

# ============================================================
# Geographic Regions
# ============================================================

REGIONS = [

    "North America",
    "South America",
    "Europe",
    "United Kingdom",
    "Middle East",
    "Africa",
    "India",
    "Singapore",
    "Japan",
    "South Korea",
    "Australia",

]

# ============================================================
# Departments
# ============================================================

DEPARTMENTS = [

    "AI Research",
    "Machine Learning",
    "Data Science",
    "Platform",
    "Cloud Engineering",
    "Infrastructure",
    "Security",
    "Analytics",
    "Computer Vision",
    "Natural Language Processing",
    "Speech AI",
    "MLOps",
    "DevOps",
    "Research",
    "Healthcare AI",
    "Autonomous Driving",

]

# ============================================================
# User Roles
# ============================================================

ROLES = [

    "Research Scientist",
    "ML Engineer",
    "Data Scientist",
    "Software Engineer",
    "Cloud Engineer",
    "MLOps Engineer",
    "DevOps Engineer",
    "Platform Engineer",
    "AI Architect",
    "Intern",

]

# ============================================================
# QoS Levels
# ============================================================

QOS_LEVELS = [

    "LOW",
    "STANDARD",
    "PREMIUM",
    "CRITICAL",

]

# ============================================================
# Priority Classes
# ============================================================

PRIORITY_LEVELS = [

    "LOW",
    "MEDIUM",
    "HIGH",
    "URGENT",

]

# ============================================================
# Customer Accounts
# ============================================================

ACCOUNTS = [

    f"ACCOUNT-{i:03d}"

    for i in range(1, 21)

]

# ============================================================
# Customer Departments
# ============================================================

CUSTOMER_DEPARTMENTS = [

    "Research",
    "Engineering",
    "Infrastructure",
    "Security",
    "Analytics",
    "Operations",
    "AI Platform",
    "Product",
    "Innovation",

]

# ============================================================
# Cluster Partitions
# ============================================================

PARTITIONS = [

    "cpu",

    "gpu-small",

    "gpu-medium",

    "gpu-large",

    "a100",

    "h100",

    "h200",

    "b200",

    "l40s",

]

# ============================================================
# License Pools
# ============================================================

LICENSES = [

    "CUDA",

    "TensorRT",

    "cuDNN",

    "NVIDIA AI Enterprise",

    "PyTorch Enterprise",

    "RAPIDS",

    "Triton",

    "None",

]

# ============================================================
# Flags
# ============================================================

FLAGS = [

    "NONE",

    "PREEMPTIBLE",

    "EXCLUSIVE",

    "CHECKPOINT",

    "RESTARTABLE",

    "HIGH_MEMORY",

]

# ============================================================
# Exit Codes
# ============================================================

EXIT_CODES = [

    0,

    1,

    137,

    143,

]

# ============================================================
# Slurm-style Job States
# ============================================================

JOB_STATES = [

    "PENDING",

    "QUEUED",

    "ALLOCATED",

    "RUNNING",

    "COMPLETING",

    "COMPLETED",

    "FAILED",

    "CANCELLED",

]

# ============================================================
# Time Limits (Minutes)
# ============================================================

TIME_LIMITS = [

    30,

    60,

    120,

    240,

    480,

    720,

    1440,

    2880,

]

# ============================================================
# Scheduler Policies
# ============================================================

SCHEDULERS = [

    "FCFS",

    "ROUND_ROBIN",

    "LEAST_LOADED",

    "BEST_FIT",

    "AI",

]

# ============================================================
# Cluster Names
# ============================================================

CLUSTERS = [

    "DGX-Cloud-01",

    "Enterprise-GPU-01",

    "Research-GPU-01",

    "Inference-Cluster",

    "Training-Cluster",

]

# ============================================================
# Common AI Models
# ============================================================

MODEL_NAMES = [

    "Llama-3-70B",

    "Llama-3-8B",

    "Mixtral-8x7B",

    "Mistral-7B",

    "DeepSeek-V3",

    "Qwen2.5-72B",

    "Phi-4",

    "Gemma-3",

    "Stable-Diffusion-XL",

    "Whisper-Large",

    "CLIP",

    "SAM-2",

]

ORGANIZATIONS = [

    "IBM AI",

    "NVIDIA Research",

    "AMD AI",

    "OpenAI",

    "Microsoft AI",

    "Google DeepMind",

    "Meta AI",

    "Databricks",

    "Snowflake",

    "Oracle",

    "Amazon",

    "Healthcare AI",

    "Retail ML",

    "Finance AI",

    "University Research",

    "Autonomous Systems",

    "Bioinformatics Lab",

    "Vision AI",

    "Robotics Group",

    "Government HPC"

]


INDUSTRIES = [

    "Healthcare",

    "Finance",

    "Retail",

    "Research",

    "Manufacturing",

    "Telecommunications",

    "Education",

    "Automotive"

]


DEPARTMENTS = [

    "Research",

    "AI Platform",

    "Data Engineering",

    "Computer Vision",

    "NLP",

    "Infrastructure",

    "Security",

    "ML Operations",

    "Cloud",

    "Analytics"

]
"""
Deployment Regions
"""

REGIONS = [

    "US-East",

    "US-West",

    "Europe",

    "India",

    "Japan",

    "Singapore",

    "Australia",

    "Middle-East"

]
