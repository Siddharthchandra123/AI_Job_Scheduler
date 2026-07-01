"""
Enterprise AI Dataset Catalog

Represents datasets commonly used for AI training,
fine-tuning, benchmarking and inference.
"""

DATASET_CATALOG = {

    "ImageNet": {
        "domain": "Computer Vision",
        "size_tb": 1.3,
        "samples": 14000000,
        "recommended_task": "Training",
        "storage_type": "Object Storage"
    },

    "COCO": {
        "domain": "Computer Vision",
        "size_tb": 0.5,
        "samples": 330000,
        "recommended_task": "Detection",
        "storage_type": "Object Storage"
    },

    "LAION-5B": {
        "domain": "Vision-Language",
        "size_tb": 240,
        "samples": 5800000000,
        "recommended_task": "Training",
        "storage_type": "Distributed Storage"
    },

    "Common Crawl": {
        "domain": "Text",
        "size_tb": 500,
        "samples": 3000000000,
        "recommended_task": "LLM Training",
        "storage_type": "Distributed Storage"
    },

    "FineWeb": {
        "domain": "LLM",
        "size_tb": 45,
        "samples": 1500000000,
        "recommended_task": "Pretraining",
        "storage_type": "Distributed Storage"
    },

    "C4": {
        "domain": "Language",
        "size_tb": 13,
        "samples": 365000000,
        "recommended_task": "Language Modeling",
        "storage_type": "Distributed Storage"
    },

    "PubMed": {
        "domain": "Healthcare",
        "size_tb": 3,
        "samples": 38000000,
        "recommended_task": "Medical LLM",
        "storage_type": "Object Storage"
    },

    "LibriSpeech": {
        "domain": "Speech",
        "size_tb": 0.3,
        "samples": 1000,
        "recommended_task": "Speech Recognition",
        "storage_type": "Object Storage"
    },

    "WikiText-103": {
        "domain": "Language",
        "size_tb": 0.1,
        "samples": 1800000,
        "recommended_task": "Language Modeling",
        "storage_type": "Object Storage"
    },

    "Enterprise-Customer-360": {
        "domain": "Enterprise",
        "size_tb": 25,
        "samples": 500000000,
        "recommended_task": "RAG",
        "storage_type": "Lakehouse"
    },

    "Fraud-Transactions": {
        "domain": "Finance",
        "size_tb": 4,
        "samples": 90000000,
        "recommended_task": "Classification",
        "storage_type": "Lakehouse"
    },

    "Healthcare-EHR": {
        "domain": "Healthcare",
        "size_tb": 18,
        "samples": 250000000,
        "recommended_task": "Prediction",
        "storage_type": "Lakehouse"
    }

}
