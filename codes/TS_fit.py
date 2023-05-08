#!/usr/bin/env python
#%%
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.optimize import differential_evolution
from sklearn.metrics import mean_squared_error
thr=100
#%% Differential equation to fit
def LotVol(t,x,a):
    x_1,x_2 = x
    r_1,r_2,a_12,a_21,K_1,K_2 = a
    dx_1 = r_1*(1-x_1/K_1-a_12*x_2/K_1)
    dx_2 = r_2*(1-a_21*x_2/K_2-x_1/K_2)
    return np.array([dx_1,dx_2])
#%% Objective function
def SSE(a,df,f):
    # Timepoints from actual data
    t=df['t'].values
    # Actual y values
    y_a= df.loc[:,['GFP','RFP']].values
    # Initial condition
    y0=y_a[0]
    # Time range to solve for (range of given data)
    trang=(t[0],t[-1])
    # Solve differetial equation 
    sol=solve_ivp(LotVol,trang,y0,t_eval=t,args=(a,f))
    # Get 'fit' equation
    y_f=sol.y.T
    # Get sum of square error
    if y_f.shape==y_a.shape:
        return mean_squared_error(y_a,y_f)
    # Return nan if solver error
    else:
        return np.nan
#%% Main function for minimizing 
def de_fit(f,fname):
    #%% Read input data
    df=pd.read_csv('../input/'+fname+'.csv')
    cname=np.array(['r_1','r_2','K_1','K_2','a_12','a_21'],dtype=str)
    filename='../output/'+fname+'-parm.csv'
    # %%
    bounds=np.full([11,2],[0,10])
    res=differential_evolution(SSE,bounds,args=(df,f),init='sobol',workers=thr,updating='deferred')
    # %%
    df=pd.DataFrame([res.x],columns=cname)
    df.to_csv(filename,index=False)
# %%
