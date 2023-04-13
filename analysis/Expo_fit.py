#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    print(file)
    if 'fc' in file:
        fc=True
    else:
        fc=False
    exp_fit(df,file,E_set,fc)
# %%
