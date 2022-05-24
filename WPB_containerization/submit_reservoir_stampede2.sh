#!/bin/bash

#SBATCH -J reservoir
#SBATCH -N 2
#SBATCH -n 48
#SBATCH -p skx-dev
#SBATCH -t 00:02:00

module load tacc-singularity
mpirun singularity run cython_reservoir_0.1.sif run_reservoir_sim.py
