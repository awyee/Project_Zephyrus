Created 2018/11/22 by Alexander Yee

REsurety Application Coding Skills Assessment

Please read Explanation_of-Approach_and_Results_Review.txt for comments requested in assignment.
To replicate results, run main.py in the Python Code folder followed by create_price_graphs. Code was run using Python 3.

Contained in the Python Code folder:
	main.py:
		Requires cvxopt, NumPy and pandas packages
		This script processes the information contained in the Input Data folder into PQ pair blocks and dispatches the blocks using the solver in the CVXOPT package.
		The market price is generated from the lambda/Lagrange multiplier of the load equality constraint (i.e. marginal cost to procure another MWh of power)

	create_price_graphs.py:
		Requires Seaborn and MatPlotLib packages
		This script takes the output of main.py and visualizes it into a graph

Contained in the Output Data folder:
	Output of main.py

Contained in the Input Data folder:
	Data received from REsurety