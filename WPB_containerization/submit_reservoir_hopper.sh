#!/bin/bash

#SBATCH -J reservoir
#SBATCH -N 1
#SBATCH -n 40
#SBATCH -p normal
#SBATCH -t 00:10:00

module load singularity
mpirun singularity run cython_reservoir_0.2.sif run_reservoir_sim.py
