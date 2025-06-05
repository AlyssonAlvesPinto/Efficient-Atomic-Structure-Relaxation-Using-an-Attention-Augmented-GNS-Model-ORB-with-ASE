## 📌 Overview

This project provides a fast and accurate script for structural relaxation of atomic systems using the ORB model—an attention-augmented Graph Network-based Simulator (GNS) . ORB is a type of Message Passing Neural Network (MPNN) that uses orbital features to predict forces and energies with high fidelity.

By leveraging ASE (Atomic Simulation Environment) and the pre-trained ORB force field, this script enables reliable relaxation of atomic structures, suitable for rapid screening or high-throughput simulations.


# ORB Structure Relaxation

Relax atomic structures using pre-trained neural network models from [ORB-models](https://github.com/orbital-materials/orb-models), integrated with the [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/).


This project uses a pre-trained ORB model to perform structural relaxation on atomic systems. The relaxation process is carried out with the BFGS optimizer in ASE. It supports both CPU and CUDA devices.




































# Orbital-Based Relaxation with ORB Model and ASE

This project performs a structural relaxation using the pre-trained ORB (Orbital Regression Based) force field model in combination with the Atomic Simulation Environment (ASE).

## 💪 Requirements

* Python 3.8+
* ASE
* NumPy
* Matplotlib
* `orb_models` (from ORB GitHub repository)

## 📦 Installation

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📂 Files and Folders

* `data/structure.vasp` – Input structure for relaxation.
* `src/relax_orb.py` – Main Python script to perform structure relaxation.
* `outputs/` – Contains the relaxed structure and plots.

## 🚀 How to Run

Run the relaxation script:

```bash
python src/relax_orb.py
```

This will generate:

* `outputs/final_structure.vasp`
* `outputs/neb_relaxation_plots.pdf`
* `outputs/go_orb.traj`

## 📈 Output Example

The relaxation plot shows the evolution of maximum force per step:

![Fmax Plot](outputs/neb_relaxation_plots.pdf)

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Citation

If you use the ORB model in your research or projects, please cite the following work:

> Benjamin Rhodes, Sander Vandenhaute, Vaidotas Šimkus, James Gin, Jonathan Godwin, Tim Duignan, and Mark Neumann.
> **Orb-v3: atomistic simulation at scale**.
> *arXiv:2504.06231*, 2025.
> [https://arxiv.org/abs/2504.06231](https://arxiv.org/abs/2504.06231)

BibTeX:

```bibtex
@misc{rhodes2025orbv3atomisticsimulationscale,
  title={Orb-v3: atomistic simulation at scale},
  author={Benjamin Rhodes and Sander Vandenhaute and Vaidotas {\v{S}}imkus and James Gin and Jonathan Godwin and Tim Duignan and Mark Neumann},
  year={2025},
  eprint={2504.06231},
  archivePrefix={arXiv},
  primaryClass={cond-mat.mtrl-sci},
  url={https://arxiv.org/abs/2504.06231},
}
```
