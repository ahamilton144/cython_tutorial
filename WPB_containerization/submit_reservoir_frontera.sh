#!/bin/bash

#SBATCH -J reservoir
#SBATCH -N 2
#SBATCH -n 56
#SBATCH -p development
#SBATCH -t 00:02:00

module load tacc-singularity
ibrun singularity run cython_reservoir_0.1.sif run_reservoir_sim.py
