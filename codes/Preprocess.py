#%%
import numpy as np
import pandas as pd
#%% Experimental set
exp_set = 'set 3 coculture compiled'
#%% Read GFP and RFP
gfp = pd.read_excel('../input/'+exp_set+'.xlsx',sheet_name='GFP')
rfp = pd.read_excel('../input/'+exp_set+'.xlsx',sheet_name='RFP')
#%% Replace space with _ for easy access
exp_set=exp_set.replace(' ','_')
# time (in days) from raw data
dayz = gfp.iloc[:,0].values
# %%
j=1
for i in range(1,gfp.shape[1]):
    col = gfp.columns[i]
    # Add replicates numbers 
    if 'Unnamed' in col:
        col = gfp.columns[i-1]
        j+=1
    else:
        j=1
    # If 
    if '+' in col:
        # Intensity levels from raw data
        g = gfp.iloc[:,i].values
        r = rfp.iloc[:,i].values
        # Create a dataframe from GFP and RFP intensity values
        df = pd.DataFrame({'t': dayz ,'GFP': g, 'RFP': r})
        col = col.replace(' ','_')
        # Save to file
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'.csv'
        df.to_csv(fname,index=False)
        # Normalize to day 1 for fold change
        df.iloc[:,1:] = df.iloc[:,1:].div(df.iloc[0,1:])
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'-fc.csv'
        df.to_csv(fname,index=False)
    else:
        # Get GFP monoculture
        g = gfp.iloc[:,i].values
        # There is no RFP
        r = np.zeros_like(g)
        # Create a dataframe from GFP and RFP intensity values
        df = pd.DataFrame({'t': dayz ,'GFP': g, 'RFP': r})
        col = col.replace(' ','_')
        # Save to file
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'.csv'
        df.to_csv(fname,index=False)
        # Normalize to day 1 for fold change
        df.iloc[:,1] = df.iloc[:,1].div(df.iloc[0,1])
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'-fc.csv'
        df.to_csv(fname,index=False)
        # Do the same for RFP
        r = rfp.iloc[:,i].values
        col = rfp.columns[i]
        # No GFP intensity
        g = np.zeros_like(r)
        # Create a dataframe from GFP and RFP intensity values
        df = pd.DataFrame({'t': dayz ,'GFP': g, 'RFP': r})
        col = col.replace(' ','_')
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'.csv'
        df.to_csv(fname,index=False)
        # Normalize to day 1 for fold change
        df.iloc[:,2] = df.iloc[:,2].div(df.iloc[0,2])
        fname = '../input/'+exp_set+'/'+col+'-'+str(j)+'-fc.csv'
        df.to_csv(fname,index=False)

