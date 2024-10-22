import os
import numpy as np
from ase.io import read, write
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter
from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator
import matplotlib.pyplot as plt

# Configure device (can be 'cpu' or 'cuda')
device = 'cuda'  # or 'cpu'

# Load the pre-trained ORB model
orbff = pretrained.orb_v2(device=device)

# Read the structure from the 'test.vasp' file using ASE
atoms = read('structure.vasp', index='-1')

# Center the atoms along the z-axis
atoms.center(axis=2)

# Set ORB as the calculator for the atoms
calc = ORBCalculator(orbff, device=device)
atoms.set_calculator(calc)

# Apply unit cell filter to relax only in the xx, yy, zz directions
ucf = ExpCellFilter(atoms, hydrostatic_strain=True)

# Initialize lists to store data for plotting
fmax_list = []
energy_list = []
step_list = []

# Callback function to collect data during optimization
def log_fmax_and_energy():
    fmax = np.max(np.abs(atoms.get_forces()))
    energy = atoms.get_potential_energy()
    fmax_list.append(fmax)
    energy_list.append(energy)
    step_list.append(len(fmax_list))

# Use the BFGS optimizer for structure relaxation
dyn = BFGS(ucf, trajectory='go_orb.traj', logfile='opt.log')
dyn.attach(log_fmax_and_energy, interval=1)
dyn.run(fmax=0.01)  # Run relaxation until the maximum force is below 10 meV/Å

# Write the relaxed geometry to 'go_cleaned_orb.vasp'
atoms.write('final_structure.vasp')

# Generate the plots
plt.figure(figsize=(10, 8))

# Plot: Step vs Fmax
plt.plot(step_list, fmax_list, 'r-o')
plt.xlabel('Step')
plt.ylabel('Fmax (eV/Å)')
plt.title('Fmax vs Step')
plt.grid(True)

# Save the plots as a PDF
plt.tight_layout()
plt.savefig('neb_relaxation_plots.pdf')

# Show the plots (optional)
plt.show()
