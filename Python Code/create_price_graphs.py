#Created 2018/11/22 by Alexander Yee

import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import os

WindCF=0.3
inputfolder = '../Output_Data'
inputpricefile='MCP_Wind_'+str(WindCF)+'.csv'
outputfolder = '../'
outputfile='MCP_Wind_'+str(WindCF)+'.jpg'

# Import Files and add Hour Ending Column
Price_data = pd.read_csv(os.path.join(inputfolder, inputpricefile))


plt.plot('HE','MCP', data=Price_data, marker='o', color='mediumvioletred')
plt.title('Estimated MCPs for ERCOT on 5/5/2016')
plt.xlabel('Hour Ending')
plt.ylabel('Markeet Clearing Price ($/MWh)')
plt.xlim(1,24)
plt.savefig(os.path.join(outputfolder,outputfile))