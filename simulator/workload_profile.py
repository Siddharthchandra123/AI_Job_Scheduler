WORKLOADS = {

    "training": {

        "weight": 25,

        "runtime": (180,720),

        "gpus": (4,16),

        "memory": (128,512),

        "priority": ["PREMIUM","CRITICAL"]

    },

    "finetuning": {

        "weight":15,

        "runtime":(30,240),

        "gpus":(1,8),

        "memory":(64,256),

        "priority":["STANDARD","PREMIUM"]

    },

    "inference":{

        "weight":35,

        "runtime":(1,20),

        "gpus":(1,2),

        "memory":(8,32),

        "priority":["LOW","STANDARD"]

    },

    "embedding":{

        "weight":10,

        "runtime":(5,60),

        "gpus":(1,2),

        "memory":(16,64),

        "priority":["STANDARD"]

    },

    "evaluation":{

        "weight":5,

        "runtime":(10,90),

        "gpus":(1,2),

        "memory":(16,64),

        "priority":["STANDARD"]

    },

    "preprocessing":{

        "weight":5,

        "runtime":(30,180),

        "gpus":(0,1),

        "memory":(32,128),

        "priority":["LOW"]

    },

    "hyperparameter_search":{

        "weight":5,

        "runtime":(240,1440),

        "gpus":(8,32),

        "memory":(256,1024),

        "priority":["CRITICAL"]

    }

}
