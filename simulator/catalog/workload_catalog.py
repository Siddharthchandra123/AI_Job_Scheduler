"""
Enterprise AI Workload Catalog

Phase-1 (Single Node HPC Scheduler)

All workloads are guaranteed to fit on a
single compute node.

Cluster Limits
--------------
CPU    : 96 cores
RAM    : 1024 GB
GPU    : 8 GPUs
"""

WORKLOADS = [

    # ==========================================================
    # LLM Fine-Tuning
    # ==========================================================

    {
        "name": "LoRA Fine-Tuning",
        "type": "finetuning",
        "description": "Parameter-efficient LLM fine-tuning",

        "runtime_min": 30,
        "runtime_max": 240,

        "gpu_min": 1,
        "gpu_max": 4,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 64,
        "memory_max": 256,
    },

    {
        "name": "Instruction Tuning",
        "type": "finetuning",
        "description": "Instruction dataset tuning",

        "runtime_min": 60,
        "runtime_max": 480,

        "gpu_min": 2,
        "gpu_max": 8,

        "cpu_min": 16,
        "cpu_max": 64,

        "memory_min": 128,
        "memory_max": 512,
    },

    # ==========================================================
    # Training
    # ==========================================================

    {
        "name": "Medium LLM Training",
        "type": "training",
        "description": "Single-node transformer training",

        "runtime_min": 240,
        "runtime_max": 1440,

        "gpu_min": 4,
        "gpu_max": 8,

        "cpu_min": 32,
        "cpu_max": 96,

        "memory_min": 256,
        "memory_max": 1024,
    },

    {
        "name": "CNN Training",
        "type": "training",
        "description": "Computer Vision model training",

        "runtime_min": 60,
        "runtime_max": 720,

        "gpu_min": 1,
        "gpu_max": 4,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 64,
        "memory_max": 256,
    },

    {
        "name": "Speech Model Training",
        "type": "training",
        "description": "Speech recognition model",

        "runtime_min": 120,
        "runtime_max": 720,

        "gpu_min": 2,
        "gpu_max": 4,

        "cpu_min": 16,
        "cpu_max": 48,

        "memory_min": 64,
        "memory_max": 256,
    },

    # ==========================================================
    # Inference
    # ==========================================================

    {
        "name": "Production Inference",
        "type": "inference",
        "description": "Online serving endpoint",

        "runtime_min": 5,
        "runtime_max": 60,

        "gpu_min": 1,
        "gpu_max": 2,

        "cpu_min": 4,
        "cpu_max": 16,

        "memory_min": 16,
        "memory_max": 64,
    },

    {
        "name": "Batch Inference",
        "type": "inference",
        "description": "Offline inference jobs",

        "runtime_min": 15,
        "runtime_max": 180,

        "gpu_min": 1,
        "gpu_max": 4,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 32,
        "memory_max": 128,
    },

    # ==========================================================
    # Embeddings
    # ==========================================================

    {
        "name": "Embedding Generation",
        "type": "embedding",

        "description": "Sentence embedding generation",

        "runtime_min": 10,
        "runtime_max": 120,

        "gpu_min": 0,
        "gpu_max": 2,

        "cpu_min": 4,
        "cpu_max": 16,

        "memory_min": 16,
        "memory_max": 64,
    },

    # ==========================================================
    # RAG
    # ==========================================================

    {
        "name": "Vector Index Build",
        "type": "rag",

        "description": "Vector database indexing",

        "runtime_min": 30,
        "runtime_max": 240,

        "gpu_min": 0,
        "gpu_max": 2,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 32,
        "memory_max": 128,
    },

    {
        "name": "Document Chunking",
        "type": "rag",

        "description": "RAG preprocessing",

        "runtime_min": 15,
        "runtime_max": 120,

        "gpu_min": 0,
        "gpu_max": 1,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 16,
        "memory_max": 64,
    },

    # ==========================================================
    # Evaluation
    # ==========================================================

    {
        "name": "Model Evaluation",
        "type": "evaluation",

        "description": "Benchmark trained checkpoints",

        "runtime_min": 20,
        "runtime_max": 120,

        "gpu_min": 1,
        "gpu_max": 2,

        "cpu_min": 4,
        "cpu_max": 16,

        "memory_min": 16,
        "memory_max": 64,
    },

    # ==========================================================
    # RLHF
    # ==========================================================

    {
        "name": "RLHF Training",
        "type": "rlhf",

        "description": "Preference optimization",

        "runtime_min": 180,
        "runtime_max": 960,

        "gpu_min": 4,
        "gpu_max": 8,

        "cpu_min": 32,
        "cpu_max": 96,

        "memory_min": 256,
        "memory_max": 1024,
    },

    # ==========================================================
    # Data Engineering
    # ==========================================================

    {
        "name": "Feature Engineering",
        "type": "preprocessing",

        "description": "Dataset feature pipeline",

        "runtime_min": 20,
        "runtime_max": 180,

        "gpu_min": 0,
        "gpu_max": 1,

        "cpu_min": 8,
        "cpu_max": 32,

        "memory_min": 32,
        "memory_max": 128,
    },

    {
        "name": "Data Cleaning",
        "type": "preprocessing",

        "description": "Data preprocessing",

        "runtime_min": 10,
        "runtime_max": 120,

        "gpu_min": 0,
        "gpu_max": 1,

        "cpu_min": 4,
        "cpu_max": 16,

        "memory_min": 16,
        "memory_max": 64,
    },

    # ==========================================================
    # Hyperparameter Search
    # ==========================================================

    {
        "name": "Hyperparameter Search",
        "type": "optimization",

        "description": "Bayesian hyperparameter optimization",

        "runtime_min": 60,
        "runtime_max": 480,

        "gpu_min": 1,
        "gpu_max": 4,

        "cpu_min": 16,
        "cpu_max": 64,

        "memory_min": 64,
        "memory_max": 256,
    }

]