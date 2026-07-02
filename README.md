# 🚀 AI Cloud Scheduler Simulator

> Enterprise-grade AI/HPC Cluster Simulator for Intelligent GPU Scheduling

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-success)
![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Overview

AI Cloud Scheduler is an enterprise-scale event-driven HPC simulation platform designed to generate realistic scheduling workloads for AI, ML, LLM, RAG and HPC environments.

Unlike a traditional scheduler, this project is designed to become a complete research platform capable of:

- Simulating AI clusters
- Generating millions of synthetic scheduling events
- Training ML-based scheduling models
- Supporting Reinforcement Learning schedulers
- Powering future Agentic AI scheduling systems

---

# Current Progress

## ✅ Phase 1 — Simulation Core (Completed)

### Infrastructure

- Account Generator
- User Generator
- GPU Generator
- Node Generator
- Cluster Generator
- Job Generator

### Enterprise Entities

- Account
- User
- GPU
- Node
- Cluster
- Job

### Event Engine

- Event Queue (Priority Queue)
- Event Dispatcher
- Event Factory
- Event Types
- Simulation Clock

### Simulation Engine

- Simulation Context
- Simulation Builder
- Simulation Runner
- Event Processing Loop

### Scheduling

- FCFS Scheduler
- Scheduler Manager
- Resource Manager

### Cluster

- Cluster State Builder
- Dynamic Resource Allocation
- Resource Release
- Runtime State Tracking

---

# Current Architecture

```
                    Job Generator
                          │
                          ▼
                  Event Queue (Heap)
                          │
                          ▼
                 Simulation Engine
                          │
                Event Dispatcher
                          │
     ┌──────────────┬──────────────┐
     ▼              ▼              ▼
 Job Submitted  Job Started  Job Completed
        │            │             │
        └────────────┴─────────────┘
                     │
                     ▼
             Scheduler Manager
                     │
                     ▼
              FCFS Scheduler
                     │
                     ▼
             Resource Manager
                     │
                     ▼
               Cluster State
                     │
                     ▼
                 Compute Nodes
```

---

# Event Lifecycle

Every job follows the complete enterprise lifecycle.

```
Job Generated
      │
      ▼
JOB_SUBMITTED
      │
      ▼
Scheduler Tick
      │
      ▼
Resource Allocation
      │
      ▼
JOB_STARTED
      │
      ▼
Runtime Simulation
      │
      ▼
JOB_COMPLETED
      │
      ▼
Resource Release
      │
      ▼
Scheduler Tick
      │
      ▼
Next Job
```

---

# Current Features

## Enterprise Job Model

Each generated job includes

- Owner
- Organization
- Department
- Region
- Workload Type
- Framework
- Model Name
- Dataset
- Resource Requirements
- Runtime
- Priority
- QoS
- Scheduler Policy
- GPU Metrics
- CPU Metrics
- Energy Metrics
- Carbon Metrics

---

## AI Workloads

Supported workload categories

- LLM Training
- LoRA Fine-tuning
- Instruction Tuning
- CNN Training
- Speech Training
- Production Inference
- Batch Inference
- Embedding Generation
- RAG Index Build
- Document Processing
- RLHF Training
- Hyperparameter Optimization
- Data Engineering
- Model Evaluation

---

## Cluster Simulation

Supports simulation of

- Multiple Nodes
- CPUs
- RAM
- GPUs
- Partitions
- Resource Allocation
- Resource Release
- Cluster State Updates

---

# Project Structure

```
AICloudScheduler/

│
├── simulator/
│
├── builders/
├── catalog/
├── engine/
├── entities/
├── events/
├── generators/
├── handlers/
├── runner/
├── state/
├── tests/
│
├── scheduler/
│
├── fcfs_scheduler.py
├── scheduler_manager.py
│
└── run.py
```

---

# Technologies

- Python 3.12
- Dataclasses
- Event Driven Architecture
- Priority Queue (heapq)
- Object Oriented Design
- Enterprise Simulation Patterns

---

# Example Simulation

```
Initializing Simulation Engine...

Simulation Engine Ready.

Starting Simulation...

Job Submitted

↓

Scheduler Tick

↓

Job Scheduled

↓

Job Started

↓

Job Completed

↓

Resources Released

↓

Simulation Completed
```

---

# Phase 1 Achievements

✅ Event Driven Architecture

✅ Dynamic Resource Allocation

✅ Resource Release

✅ Cluster State Tracking

✅ Enterprise Job Model

✅ Job Generator

✅ Event Queue

✅ Dispatcher

✅ Simulation Engine

✅ FCFS Scheduler

---

# Roadmap

## Phase 2 — Analytics Engine

Planned modules

```
analytics/

metrics.py

collector.py

statistics.py

reward.py

feature_extractor.py

dataset_builder.py

exporter.py
```

Features

- Queue Metrics
- GPU Utilization
- CPU Utilization
- Cluster Utilization
- Throughput
- Waiting Time
- Turnaround Time
- Energy Consumption
- Carbon Emissions

---

## Phase 3 — Dataset Generation

Generate datasets for

- Random Forest
- XGBoost
- LightGBM
- CatBoost
- Deep Learning
- Reinforcement Learning

Export formats

- CSV
- Parquet
- JSON

---

## Phase 4 — Intelligent Scheduling

Schedulers to implement

- Shortest Job First
- Priority Scheduler
- Backfilling
- Dominant Resource Fairness (DRF)
- Fair Share Scheduler
- AI Scheduler

---

## Phase 5 — Machine Learning Scheduler

Train models using simulator-generated datasets.

Models

- Random Forest
- XGBoost
- LightGBM
- Transformer
- Graph Neural Networks
- PPO
- Deep Reinforcement Learning

---

## Phase 6 — Agentic AI Scheduler

Future capabilities

- LLM Scheduler
- Multi-Agent Scheduling
- Autonomous Cluster Management
- Predictive Resource Allocation
- Self-Healing Scheduling
- Explainable Scheduling Decisions

---

# Long-Term Vision

```
Synthetic Job Generator
        │
        ▼
Event Driven HPC Simulator
        │
        ▼
Metrics Collection
        │
        ▼
Feature Engineering
        │
        ▼
Training Dataset
        │
        ▼
Machine Learning Models
        │
        ▼
AI Scheduler
        │
        ▼
Agentic AI Cluster Manager
```

---

# Current Status

| Component | Status |
|-----------|--------|
| Entity Layer | ✅ Complete |
| Generator Layer | ✅ Complete |
| Event Engine | ✅ Complete |
| Scheduler | ✅ FCFS Complete |
| Resource Manager | ✅ Complete |
| Simulation Engine | ✅ Complete |
| Cluster State | ✅ Complete |
| Analytics | 🚧 Next Phase |
| Dataset Generation | 🚧 Planned |
| AI Scheduler | 🚧 Planned |
| RL Scheduler | 🚧 Planned |
| Agentic AI | 🚧 Planned |

---

# Author

**Siddharth Chandra**

AI/ML Engineer | HPC | Distributed Systems | LLM | Agentic AI | GPU Scheduling

GitHub:
https://github.com/Siddharthchandra123