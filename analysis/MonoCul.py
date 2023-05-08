#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams["svg.hashsalt"]=''
plt.rcParams["font.size"]=22
# %% Sens
gfp = pd.read_csv('../input/set_3_coculture_compiled/O3_GFP-1-fc.csv')
rfp = pd.read_csv('../input/set_3_coculture_compiled/O3_RFP-1-fc.csv')
repl = pd.read_csv('../input/set_3_coculture_compiled/O3_GFP.1-1-fc.csv')
# %%
fig=plt.figure(figsize=(15,10))
plt.plot(gfp['t'],gfp['GFP'],c='tab:green',label='GFP')
plt.plot(rfp['t'],rfp['RFP'],c='tab:red',label='RFP')
plt.plot(repl['t'],repl['GFP'],c='tab:green',linestyle='dashed',label='GFP-2')
# Matplotlib label stuff
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Fold Change')
plt.title('Sensitive')
plt.tight_layout()
figname='../figures/Sensitive-monoculture.svg'
plt.savefig(figname)
plt.close(fig) 
# %% Rest
gfp = pd.read_csv('../input/set_3_coculture_compiled/A13_GFP-1-fc.csv')
rfp = pd.read_csv('../input/set_3_coculture_compiled/A13_RFP-1-fc.csv')
repl = pd.read_csv('../input/set_3_coculture_compiled/A13_RFP.1-1-fc.csv')
# %%
fig=plt.figure(figsize=(15,10))
plt.plot(gfp['t'],gfp['GFP'],c='tab:green',label='GFP')
plt.plot(rfp['t'],rfp['RFP'],c='tab:red',label='RFP')
plt.plot(repl['t'],repl['RFP'],c='tab:red',linestyle='dashed',label='RFP-2')
# Matplotlib label stuff
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Fold Change')
plt.title('Resistant')
plt.tight_layout()
figname='../figures/Resistant-monoculture.svg'
plt.savefig(figname)
plt.close(fig) 

# %%
