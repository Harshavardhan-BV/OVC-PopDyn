#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common_fn import *
from glob import glob
import os
#%%
E_set = 'set_3_coculture_compiled'
files=glob('../input/'+E_set+'/*-fc.csv')
#%%
for file in files:
    df = pd.read_csv(file)
    file = os.path.splitext(os.path.split(file)[1])[0]
    t_df = df_td(df,file,E_set)
    t_df[t_df[['GFP','RFP']]<=0] = 0
    plot_td(t_df,file,E_set)
# %%
