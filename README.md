# ORB Structure Relaxation

Relax atomic structures using pre-trained machine learning models from [ORB-models](https://github.com/orbital-materials/orb-models), integrated with the [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/).

## 📌 Overview

This project uses a pre-trained ORB model to perform structural relaxation on atomic systems. The relaxation process is carried out with the BFGS optimizer in ASE. It supports both CPU and CUDA devices.

## 🚀 How to Use

### 1. Install Dependencies

We recommend creating a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
