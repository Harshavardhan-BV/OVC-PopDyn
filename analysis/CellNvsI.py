#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from common_fn import *
#%% Reading input for GFP and RFP intensity
gfp = pd.read_excel('../input/set 3 coculture compiled.xlsx',sheet_name='GFP')
rfp = pd.read_excel('../input/set 3 coculture compiled.xlsx',sheet_name='RFP')
#%% Total no. of initial cells
n = 3000
#%% Proportions of gfp & rfp
gfp_prop = np.array([0.95,0.95,0.05,0.05,0.25,0.25,0.75,0.75,0.5,0.5,1])
rfp_prop = 1 - gfp_prop
rfp_prop[np.where(rfp_prop == 0)] = 1
# %% Select Intensity readings for Day 0
gfp_I = gfp.iloc[0,1:].values
rfp_I = rfp.iloc[0,1:].values
# %% Sensitive
plot_NvsI(gfp_I[0:11],rfp_I[0:11],gfp_prop,rfp_prop,n,'Sensitive')
# %% Resistant
plot_NvsI(gfp_I[11:22],rfp_I[11:22],gfp_prop,rfp_prop,n,'Resistant')
# %%
