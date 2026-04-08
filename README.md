# WARP-28round-Analysis
WARP-28round-Analysis
This repository contains the source code and experimental data for the 28-round impossible differential attack and DS-MITM (Differential States Meet-in-the-Middle) analysis on the lightweight block cipher WARP.

1. Project Introduction
In this project, we successfully identified an 18-round impossible differential distinguisher by utilizing an improved MILP (Mixed-Integer Linear Programming) model and extended the attack to 28 rounds.

3. Requirements
To run the scripts, the following environment is required:
Python 3.8+
Gurobi Optimizer (Version 9.0+ recommended)
Dependencies: numpy, gurobipy

4. File Descriptions
forward_rounds.py	Describes the 5-round forward expansion (encryption) before the distinguisher and the subkey guessing logic.
backward_rounds.py	Describes the 5-round backward expansion (decryption) after the distinguisher and the state backtracking.
complexity_calc.py	Contains the DDT (Difference Distribution Table) and MILP constraints for the WARP S-box.
permutation_layer.py	Implements the first half of the 32-branch permutation layer logic unique to WARP.
perm_step_details.py	Implements the second half of the 32-branch permutation layer logic unique to WARP.
README.md	This instruction file. 
