Structural Trap Classifier Repository
==================================

This repository contains classifiers that have been trained to predict whether certain fully-coordinated phosphorus in a quantum dot crystal structure are associated with structural trap states. If you're curious, check out the paper! (arXiv:2505.22419)

Repository Structure
--------------------
models/:     Contains (.pkl) trained scikit-learn model files.

run_model.py:     A simple python script to load a chosen model, select the appropriate set of features, and run the model to make and save predictions.
    
README.txt:     This file.


Example Usage
-----

python3 run_model.py -d my_data.csv -m models/gbt_all_p4c_all_features.pkl -o predictions.npy

Ensure that you use the correct input data format (see below).

Input Data Format
-----------------
The models expect data in excel or csv format with specific columns. 
More details on the requisite features can be found in the SI of the paper. (arXiv:2505.22419)

Required Columns:
 
 	- Participation Ratio (float)
	- State Energy (eV) (float)
	- Gating Participation Ratio (float)
	- Total Under-Coordinated Cation Alpha (float)
	- Total Fully-Coordinated Cation Alpha (float)
	- Total Under-Coordinated Anion Alpha (float)
	- Total Fully-Coordinated Anion Alpha (float)
    - Total Ligand Alpha (float)
    - Energy from HOMO (eV) (float)
    - HOMO Energy (eV) (float)
    - Cuboctahedral? (int)
    - Total # Cations (int)
    - Total # Anions (int)
    - Total # Ligand (int)
    - Total # Atoms (int)
    - Fraction of Cations that are In (int)
    - Total Charge (int)
    - HOMO-LUMO Gap (eV) (float)
    - Quantum Confined State? (int)
    - Total Dipole Moment (float)
    - Total Under-Coordinated Traps in QD (int)
    - Center Alpha (float)
    - Center Mulliken (float)
    - Center Mulliken Relative to Element Average (float)
    - Center Lowdin in State (float)
    - Center Total Lowdin (float)
    - Center Total Lowdin Relative to Element Average (float)
    - Center Dipole Overlap (float)
    - Tetrahedral Absolute Error (float)
    - Tetrahedral Squared Error (float)
    - SeeSaw Absolute Error (float)
    - SeeSaw Squared Error (float)
    - Bond Angle 1 (float)
    - Bond Angle 2 (float)
    - Bond Angle 3 (float)
    - Bond Angle 4 (float)
    - Bond Angle 5 (float)
    - Bond Angle 6 (float)
    - Relative Bond Length 1 (float)
    - Relative Bond Length 2 (float)
    - Relative Bond Length 3 (float)
    - Relative Bond Length 4 (float)
    - Neighbor 0 Coordination Number (int)
    - Neighbor 0 Distance to Center (float)
    - Neighbor 1 Coordination Number (int)
    - Neighbor 1 Distance to Center (float)
    - Neighbor 2 Coordination Number (int)
    - Neighbor 2 Distance to Center (float)
    - Neighbor 3 Coordination Number (int)
    - Neighbor 3 Distance to Center (float)


Author
------
Ezra Alexander
