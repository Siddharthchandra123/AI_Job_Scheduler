"""
Enterprise Software Stack Catalog
"""

SOFTWARE_STACK = {

    "CUDA_12_4": {
        "cuda": "12.4",
        "driver": "550.54",
        "cudnn": "9.1",
        "nccl": "2.21",
        "tensorrt": "10.2",
        "python": "3.12",
        "ubuntu": "24.04"
    },

    "CUDA_12_2": {
        "cuda": "12.2",
        "driver": "535.183",
        "cudnn": "9.0",
        "nccl": "2.20",
        "tensorrt": "10.1",
        "python": "3.11",
        "ubuntu": "22.04"
    },

    "PYTORCH_2_7": {
        "framework": "PyTorch",
        "version": "2.7",
        "torchvision": "0.22",
        "torchaudio": "2.7"
    },

    "PYTORCH_2_6": {
        "framework": "PyTorch",
        "version": "2.6",
        "torchvision": "0.21",
        "torchaudio": "2.6"
    },

    "TENSORFLOW_2_18": {
        "framework": "TensorFlow",
        "version": "2.18"
    },

    "RAY_2_48": {
        "version": "2.48"
    },

    "TRITON_25_06": {
        "version": "25.06"
    },

    "MORPHEUS_25_06": {
        "version": "25.06"
    }

}
