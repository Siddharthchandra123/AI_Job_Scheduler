"""
Quality of Service
"""

QOS_LEVELS = {

    "LOW": {

        "priority": 1,

        "max_runtime": 2,

        "preemptible": True

    },

    "STANDARD": {

        "priority": 2,

        "max_runtime": 12,

        "preemptible": False

    },

    "PREMIUM": {

        "priority": 3,

        "max_runtime": 48,

        "preemptible": False

    },

    "CRITICAL": {

        "priority": 4,

        "max_runtime": 168,

        "preemptible": False

    }

}
