# AI Cloud Scheduler

### Enterprise AI-Powered Cloud & HPC Scheduler Simulator

**Author:** Siddharth Chandra

---

# Overview

AI Cloud Scheduler is an enterprise-scale **Digital Twin** of an AI/HPC cloud environment capable of simulating millions of scheduling events for modern AI workloads.

The simulator models organizations, users, AI jobs, GPU clusters, compute nodes, and scheduling behavior. It is designed to generate realistic datasets for:

* Supervised Learning
* Reinforcement Learning
* Scheduling Research
* GPU Resource Optimization
* Kubernetes Scheduling
* NVIDIA GPU Infrastructure
* HPC Cluster Simulation

The long-term objective is to replace traditional scheduling algorithms with AI-driven scheduling policies capable of minimizing queue time, maximizing GPU utilization, reducing energy consumption, and improving overall cluster efficiency.

---

# Current Project Status

## Phase 1 — Foundation ✅ (Completed)

The foundational layer of the simulator has been implemented and successfully tested.

Completed modules include:

* Configuration Management
* Hardware Catalogs
* Organization Catalogs
* Domain Entities
* Synthetic Infrastructure Generators
* Initial Testing Pipeline

---

# Project Architecture

```
AICloudScheduler
│
├── simulator
│   ├── catalog
│   ├── config
│   ├── entities
│   ├── generators
│   ├── engine
│   ├── events
│   ├── tests
│   └── datasets
│
├── scheduler
├── backend
├── ai
├── frontend
├── monitoring
├── kubernetes
└── docs
```

---

# Completed Modules

## Configuration

Implemented:

```
simulation.yaml

loader.py
```

Provides:

* Simulation configuration
* Cluster size
* Number of jobs
* Random seed
* Hardware configuration
* Dataset configuration

---

## Catalogs

Implemented enterprise catalogs for synthetic data generation.

### GPU Catalog

Supports

* NVIDIA V100
* NVIDIA A100
* NVIDIA H100
* NVIDIA H200
* NVIDIA B200
* NVIDIA L40S

Each GPU stores

* Memory
* CUDA Version
* Power
* TFLOPS
* Failure Rate
* Hourly Cost

---

### Organization Catalog

Includes

* Organizations
* Departments
* Industries
* Projects
* Cost Centers
* User Roles
* Organization Sizes
* User Behaviour Profiles

---

### Workload Catalog

Supports

* Training
* Fine-tuning
* Inference
* Embedding
* Evaluation
* Hyperparameter Search
* Preprocessing

---

### Model Catalog

Supports enterprise AI models

Examples

* Llama 3
* DeepSeek
* Gemma
* Qwen
* Mixtral
* Stable Diffusion
* Whisper
* CLIP

Each model stores

* Parameter Count
* GPU Requirement
* Runtime
* Framework
* Memory Requirement

---

### Dataset Catalog

Supports

* ImageNet
* COCO
* LAION-5B
* Common Crawl
* FineWeb
* PubMed
* C4
* Enterprise Customer360

---

### Software Catalog

Stores

* CUDA
* cuDNN
* NCCL
* TensorRT
* PyTorch
* TensorFlow
* Ray
* Morpheus

---

# Domain Entities

Implemented

```
Account

User

GPU

Node

Partition

Cluster

Job

Workload

Enums
```

These entities represent the digital twin of a production cloud environment.

---

# Enterprise Job Entity

The Job object models an enterprise AI workload.

It currently contains fields representing

### Metadata

* Job ID
* Job Name
* Comment

### Ownership

* Account
* User
* Department
* Region
* Project
* Cost Center

### Scheduling

* QoS
* Priority
* Scheduler
* Partition
* Queue Position

### Resources

* CPU
* GPU
* Memory
* Storage
* Network

### Runtime

* Execution Time
* Wait Time
* CPU Time
* Elapsed Time
* Core Hours
* Time To Result

### AI

* Predicted Runtime
* Predicted Wait
* Reward
* Scheduler Score

### Sustainability

* GPU Energy
* Carbon Emission

---

# Synthetic Generators

Implemented

```
BaseGenerator

GPUGenerator

NodeGenerator

PartitionGenerator

ClusterGenerator

AccountGenerator

UserGenerator
```

These generators create realistic synthetic infrastructure.

---

# Infrastructure Pipeline

```
GPU Catalog

↓

GPU Generator

↓

Node Generator

↓

Partition Generator

↓

Cluster Generator

↓

Organization Generator

↓

User Generator
```

---

# Event Driven Simulation

Current progress

```
event.py

event_queue.py

event_factory.py

event_types.py
```

Implemented

* Event object
* Priority Queue
* Event Factory
* Event Types

Events supported

```
JOB_SUBMITTED

JOB_STARTED

JOB_COMPLETED

GPU_ALLOCATED

GPU_RELEASED

NODE_FAILED

NODE_RECOVERED

SIMULATION_START

SIMULATION_END

SCHEDULER_TICK
```

---

# Simulation Engine

Initial engine implemented

Modules

```
SimulationClock

SimulationContext

Dispatcher

Allocator

ResourceManager

SimulationEngine
```

Current capability

* Virtual Clock
* Priority Event Queue
* Event Dispatching
* Resource Allocation
* Simulation Loop

---

# Unit Tests

Successfully completed

```
Account Generator

User Generator

GPU Generator

Node Generator

Job Entity

Foundation Pipeline
```

---

# Current Workflow

```
Configuration
      │
      ▼
Catalogs
      │
      ▼
Entities
      │
      ▼
Generators
      │
      ▼
Simulation Context
      │
      ▼
Event Queue
      │
      ▼
Simulation Engine
```

---

# Technologies Used

## Programming

* Python 3.12

---

## AI

* PyTorch
* XGBoost
* Stable-Baselines3 (Planned)

---

## Data

* PostgreSQL
* Parquet
* Pandas

---

## Streaming

* Apache Kafka
* NVIDIA Morpheus (Planned)

---

## Infrastructure

* Kubernetes
* Kueue
* NVIDIA GPU Operator

---

## Monitoring

* Prometheus
* Grafana
* NVIDIA DCGM

---

# Upcoming Milestones

## Phase 2

Discrete Event Simulation

* Complete Event Dispatcher
* Resource Allocation Engine
* Scheduler Integration
* Simulation State Manager

---

## Phase 3

Scheduling Algorithms

* FCFS
* Round Robin
* Least Loaded
* Priority Scheduler
* Best Fit

---

## Phase 4

Synthetic Dataset Generation

Generate

* 1 Million Jobs
* 20 Organizations
* 100 Users
* Multiple Clusters
* Enterprise Scheduling Logs

---

## Phase 5

Supervised Learning

Train models for

* Node Selection
* Runtime Prediction
* Queue Prediction
* Resource Recommendation

---

## Phase 6

Reinforcement Learning

Develop an intelligent scheduler using

* PPO
* DQN
* A2C

Reward optimization based on

* GPU Utilization
* Queue Time
* Energy Consumption
* SLA Compliance

---

## Phase 7

Enterprise Deployment

Integrate with

* Apache Kafka
* NVIDIA Morpheus
* PostgreSQL
* Kubernetes
* NVIDIA Triton
* Kueue
* Prometheus
* Grafana

---

# Long-Term Vision

Develop a production-grade **AI-powered cloud scheduling platform** capable of:

* Simulating millions of enterprise AI jobs.
* Training AI models for intelligent scheduling decisions.
* Integrating with Kubernetes and NVIDIA GPU infrastructure.
* Optimizing GPU utilization, queue time, energy efficiency, and SLA compliance.
* Serving as a research and benchmarking platform for next-generation AI/HPC scheduling.

---

# Current Progress

| Module                 | Status         |
| ---------------------- | -------------- |
| Configuration          | ✅ Complete     |
| Catalogs               | ✅ Complete     |
| Domain Entities        | ✅ Complete     |
| Generators             | ✅ Complete     |
| Foundation Tests       | ✅ Complete     |
| Event System           | 🟡 In Progress |
| Simulation Engine      | 🟡 In Progress |
| Scheduling Algorithms  | ⏳ Planned      |
| Dataset Generation     | ⏳ Planned      |
| AI Training            | ⏳ Planned      |
| Reinforcement Learning | ⏳ Planned      |
| Kafka Integration      | ⏳ Planned      |
| NVIDIA Morpheus        | ⏳ Planned      |
| Kubernetes Integration | ⏳ Planned      |
| Enterprise Dashboard   | ⏳ Planned      |

---

**Current Status:** **Phase 1 Complete ✅ | Phase 2 (Discrete Event Simulation Engine) In Progress 🚧**
