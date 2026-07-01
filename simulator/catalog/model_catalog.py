"""
Enterprise AI Model Catalog

Defines popular AI models along with their typical hardware
requirements and execution characteristics.
"""

MODEL_CATALOG = {

    "Llama-3-8B": {
        "family": "Llama",
        "type": "LLM",
        "parameters_billion": 8,
        "framework": "PyTorch",
        "gpu_memory_gb": 24,
        "recommended_gpu": "L40S",
        "recommended_gpus": 1,
        "avg_training_hours": 8,
        "avg_inference_latency_ms": 120,
    },

    "Llama-3-70B": {
        "family": "Llama",
        "type": "LLM",
        "parameters_billion": 70,
        "framework": "PyTorch",
        "gpu_memory_gb": 320,
        "recommended_gpu": "H100",
        "recommended_gpus": 8,
        "avg_training_hours": 72,
        "avg_inference_latency_ms": 350,
    },

    "DeepSeek-R1": {
        "family": "DeepSeek",
        "type": "LLM",
        "parameters_billion": 671,
        "framework": "PyTorch",
        "gpu_memory_gb": 1024,
        "recommended_gpu": "B200",
        "recommended_gpus": 32,
        "avg_training_hours": 240,
        "avg_inference_latency_ms": 900,
    },

    "Qwen-3-32B": {
        "family": "Qwen",
        "type": "LLM",
        "parameters_billion": 32,
        "framework": "PyTorch",
        "gpu_memory_gb": 160,
        "recommended_gpu": "H100",
        "recommended_gpus": 4,
        "avg_training_hours": 36,
        "avg_inference_latency_ms": 280,
    },

    "Gemma-3-27B": {
        "family": "Gemma",
        "type": "LLM",
        "parameters_billion": 27,
        "framework": "PyTorch",
        "gpu_memory_gb": 128,
        "recommended_gpu": "A100",
        "recommended_gpus": 4,
        "avg_training_hours": 24,
        "avg_inference_latency_ms": 240,
    },

    "Mistral-7B": {
        "family": "Mistral",
        "type": "LLM",
        "parameters_billion": 7,
        "framework": "PyTorch",
        "gpu_memory_gb": 20,
        "recommended_gpu": "L40S",
        "recommended_gpus": 1,
        "avg_training_hours": 6,
        "avg_inference_latency_ms": 90,
    },

    "Mixtral-8x7B": {
        "family": "Mixtral",
        "type": "MoE",
        "parameters_billion": 46,
        "framework": "PyTorch",
        "gpu_memory_gb": 192,
        "recommended_gpu": "H100",
        "recommended_gpus": 8,
        "avg_training_hours": 60,
        "avg_inference_latency_ms": 300,
    },

    "Stable-Diffusion-XL": {
        "family": "Diffusion",
        "type": "Vision",
        "parameters_billion": 3.5,
        "framework": "PyTorch",
        "gpu_memory_gb": 16,
        "recommended_gpu": "L40S",
        "recommended_gpus": 1,
        "avg_training_hours": 10,
        "avg_inference_latency_ms": 450,
    },

    "CLIP": {
        "family": "Vision",
        "type": "Embedding",
        "parameters_billion": 1,
        "framework": "PyTorch",
        "gpu_memory_gb": 12,
        "recommended_gpu": "A100",
        "recommended_gpus": 1,
        "avg_training_hours": 4,
        "avg_inference_latency_ms": 80,
    },

    "Whisper-Large-v3": {
        "family": "Speech",
        "type": "ASR",
        "parameters_billion": 1.5,
        "framework": "PyTorch",
        "gpu_memory_gb": 18,
        "recommended_gpu": "L40S",
        "recommended_gpus": 1,
        "avg_training_hours": 12,
        "avg_inference_latency_ms": 160,
    }

}
