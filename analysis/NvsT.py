#%%
import numpy as np
import pandas as pd
from common_fn import *
from glob import glob
import os
#%%
E_set = 'set_3_coculture_compiled'
files=glob('../input/'+E_set+'/*.csv')
# %%
for file in files:
    df = pd.read_csv(file)
    file = os.path.splitext(file.split('/')[-1])[0] 
    if 'fc' in file:
        fc=True
    else:
        fc=False
    plot_Nvst(df,file,E_set,fc)
# %%
