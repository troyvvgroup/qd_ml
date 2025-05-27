import joblib
from optparse import OptionParser
import pandas as pd
import numpy as np

def make_predictions(df,model):

	m = joblib.load(model)

	if model == "nn_all_p4c_geometry_only.pkl":
		features = ["Cuboctahedral?", "Total # Cations", "Total # Anions", "Total # Ligand", "Total # Atoms", "Fraction of Cations that are In", "Total Charge", "Total Dipole Moment", "Center Dipole Overlap", "Tetrahedral Absolute Error", "Tetrahedral Squared Error", "SeeSaw Absolute Error", "SeeSaw Squared Error", "Bond Angle 1", "Bond Angle 2", "Bond Angle 3", "Bond Angle 4", "Bond Angle 5", "Bond Angle 6", "Relative Bond Length 1", "Relative Bond Length 2", "Relative Bond Length 3", "Relative Bond Length 4", "Neighbor 0 Coordination Number", "Neighbor 0 Distance to Center", "Neighbor 1 Coordination Number", "Neighbor 1 Distance to Center", "Neighbor 2 Coordination Number", "Neighbor 2 Distance to Center", "Neighbor 3 Coordination Number", "Neighbor 3 Distance to Center"]
	else:
		features = ["Participation Ratio", "State Energy (eV)", "Gating Participation Ratio", "Total Under-Coordinated Cation Alpha", "Total Fully-Coordinated Cation Alpha", "Total Under-Coordinated Anion Alpha", "Total Fully-Coordinated Anion Alpha", "Total Ligand Alpha", "Energy from HOMO (eV)", "HOMO Energy (eV)", "Cuboctahedral?", "Total # Cations", "Total # Anions", "Total # Ligand", "Total # Atoms", "Fraction of Cations that are In", "Total Charge", "HOMO-LUMO Gap (eV)", "Quantum Confined State?", "Total Dipole Moment", "Total Under-Coordinated Traps in QD", "Center Alpha", "Center Mulliken", "Center Mulliken Relative to Element Average", "Center Lowdin in State", "Center Total Lowdin", "Center Total Lowdin Relative to Element Average", "Center Dipole Overlap", "Tetrahedral Absolute Error", "Tetrahedral Squared Error", "SeeSaw Absolute Error", "SeeSaw Squared Error", "Bond Angle 1", "Bond Angle 2", "Bond Angle 3", "Bond Angle 4", "Bond Angle 5", "Bond Angle 6", "Relative Bond Length 1", "Relative Bond Length 2", "Relative Bond Length 3", "Relative Bond Length 4"]

	df = df[features].copy()

	X = pd.get_dummies(df)

	y_pred = m.predict(X)

	return y_pred

def load_data(data):

	if data.split('/')[-1].split('.')[-1] == "xlsx":
		df = pd.read_excel(data)
	elif data.split('/')[-1].split('.')[-1] == "csv":
		df = pd.read_csv(data)
	else:
		raise Exception("Data file type unsupported")

	return df

def main():

	parser=OptionParser()

	parser.add_option("-m","--model",dest="model", help="The file with the model you want to use, in the models/ directory. Example: '-m models/gbt_all_p4c_all_features.pkl'", action="store",type="string")
	parser.add_option("-d",'--data',dest="data",help="The file with the data you want to run the model on, in the appropriate format. Excel and csv files supported.",action="store",type="string")
	parser.add_option("-o",'--output',dest="output",help="The file name (.npy) you want to save the predictions to. ",action="store",type="string")

	(options,args) = parser.parse_args()

	df = load_data(options.data)

	predictions = make_predictions(df,options.model)

	np.save(options.output, predictions)

if __name__ == '__main__':
    main()