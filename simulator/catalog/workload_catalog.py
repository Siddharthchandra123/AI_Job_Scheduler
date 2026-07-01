"""
Enterprise AI workload definitions.
"""

WORKLOADS = {

    "training": {

        "weight": 25,

        "gpu_range": (4, 16),

        "runtime_hours": (2, 24),

        "memory_gb": (128, 1024),

        "frameworks": [

            "PyTorch",

            "TensorFlow"

        ]

    },

    "finetuning": {

        "weight": 15,

        "gpu_range": (1, 8),

        "runtime_hours": (1, 8),

        "memory_gb": (64, 512),

        "frameworks": [

            "PyTorch"

        ]

    },

    "inference": {

        "weight": 35,

        "gpu_range": (1, 2),

        "runtime_hours": (1, 2),

        "memory_gb": (8, 64),

        "frameworks": [

            "TensorRT",

            "ONNX"

        ]

    },

    "embedding": {

        "weight": 10,

        "gpu_range": (1, 2),

        "runtime_hours": (1, 3),

        "memory_gb": (16, 64),

        "frameworks": [

            "PyTorch"

        ]

    },

    "evaluation": {

        "weight": 5,

        "gpu_range": (1, 2),

        "runtime_hours": (1, 4),

        "memory_gb": (16, 64),

        "frameworks": [

            "PyTorch"

        ]

    },

    "preprocessing": {

        "weight": 5,

        "gpu_range": (0, 1),

        "runtime_hours": (1, 6),

        "memory_gb": (32, 128),

        "frameworks": [

            "RAPIDS cuML",

            "Scikit-Learn"

        ]

    },

    "hyperparameter_search": {

        "weight": 5,

        "gpu_range": (8, 32),

        "runtime_hours": (12, 72),

        "memory_gb": (512, 2048),

        "frameworks": [

            "PyTorch"

        ]

    }

}
