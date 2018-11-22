import glpk as opt
import numpy as np
import pandas as pd
import os

# Filename and Filepath declarations
inputfolder = '../Input_Data'
input_SCED_Data = 'SCED_Data.csv'
input_Demand_Data = 'DemandData.csv'
outputfolder = '../Output_Data'

# Import Files and add Hour Ending Column
SCED_data = pd.read_csv(os.path.join(inputfolder, input_SCED_Data))
Demand_data = pd.read_csv(os.path.join(inputfolder, input_Demand_Data))

SCED_data['HE'] = SCED_data['Time'].apply(lambda x: int(x.split(':')[0].split()[1]) + 1)  # HE=Hour Ending
Demand_data['HE'] = Demand_data['Time'].apply(lambda x: int(x.split(':')[0].split()[1]) + 1)

hour = 1

SCED_hour_data = SCED_data[SCED_data['HE'] == hour]
unit_list = SCED_hour_data['Resource.Name'].tolist()

PQ_list = pd.DataFrame(columns=['Unit', 'PQ Pair', 'Price', 'Quantity'])
for unit in unit_list:
    exit_loop = False
    PQ = 2
    while PQ <= 40 and exit_loop == False:
        PriceName = 'SCED1.Curve.Price' + str(PQ)
        QuantName = 'SCED1.Curve.MW' + str(PQ)
        Quantity = SCED_hour_data[SCED_hour_data['Resource.Name'] == unit][QuantName]
        Price = SCED_hour_data[SCED_hour_data['Resource.Name'] == unit][PriceName]
        if Quantity != 0:
            PQ_list.append([unit, PQ, Price, Quantity])
            PQ += 1
        else:
            exit_loop = True

lp = opt.LPX()