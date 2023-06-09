import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.rcParams["svg.hashsalt"]=''
plt.rcParams["font.size"]=22

# define linear function
def lin(x,m,c):
    return m*x+c

# define exponential function
def expo(x,y0,r):
    return y0*np.exp(r*x)

# Plot the Intensity vs Cell number
def plot_NvsI(g_I,r_I,g_prop,r_prop,n,Title):
    # Converting proportions to number
    g_prop=g_prop*n
    r_prop=r_prop*n
    xdata = np.linspace(0, n, 100)
    fig=plt.figure(figsize=(15,10))
    # Plotting GFP measurements
    plt.scatter(g_prop,g_I,c='tab:green',label='GFP')
    # Fitting line to GFP and plotting
    popt, pcov = curve_fit(lin, g_prop, g_I)
    print('GFP: m ={}, c={}'.format(*popt))
    y_fit = lin(xdata,*popt)
    plt.plot(xdata,y_fit,c='tab:green',label='GFP-linear')
    # Plotting RFP measurements
    plt.scatter(r_prop,r_I,c='tab:red',label='RFP')
    # Fitting line to RFP and plotting
    popt, pcov = curve_fit(lin, r_prop, r_I)
    print('RFP: m ={}, c={}'.format(*popt))
    y_fit = lin(xdata,*popt)
    plt.plot(xdata,y_fit,c='tab:red',label='RFP-linear')
    # Matplotlib label stuff
    plt.legend()
    plt.xlabel('Approx Cells')
    plt.ylabel('Intensity')
    plt.title(Title)
    plt.tight_layout()
    figname='../figures/'+Title+'-NvsI.svg'
    plt.savefig(figname)
    plt.close(fig) 

# Plot the Cell number vs Time
def plot_Nvst(df,Title,e_set,fc=False):
    fig=plt.figure(figsize=(15,10))
    # Plot 
    plt.plot(df['t'],df['GFP'],c='tab:green',label='GFP')
    plt.plot(df['t'],df['RFP'],c='tab:red',label='RFP')
    # Matplotlib label stuff
    plt.legend()
    plt.xlabel('Time (days)')
    if fc:
        plt.ylabel('Fold Change')
        figname='../figures/'+e_set+'/Plot/fc/'+Title+'-Nvst.svg'
    else:
        plt.ylabel('Cell count')
        figname='../figures/'+e_set+'/Plot/'+Title+'-Nvst.svg'
    plt.title(Title)
    plt.tight_layout()
    plt.savefig(figname)
    plt.close(fig) 

# 
def exp_fit(df,Title,e_set,fc):
    fig=plt.figure(figsize=(15,10))
    # tdata = np.linspace(df['t'].iloc[0], df['t'].iloc[-1], 100)
    tdata = np.linspace(df['t'].iloc[0], 20, 100)
    t=df.loc[0:4,'t'].values
    # Plot actual GFP data point
    plt.plot(df['t'],df['GFP'],c='tab:green',label='GFP')
    # Select GFP only for the initial 4 days
    IFP = df.loc[0:4,'GFP'].values
    # and fit exponential to it
    popt, pcov = curve_fit(expo, t, IFP)
    print('GFP: y0 ={}, r={}'.format(*popt))
    y_fit = expo(tdata,*popt)
    # Plot the fit for GFP
    plt.plot(tdata,y_fit,c='tab:green',linestyle='dashed',label='GFP-expo')
    # Plot actual RFP data point
    plt.plot(df['t'],df['RFP'],c='tab:red',label='RFP')
    # Select RFP only for the initial 4 days
    IFP = df.loc[0:4,'RFP'].values
    # and fit exponential to it
    popt, pcov = curve_fit(expo, t, IFP)
    print('RFP: y0 ={}, r={}'.format(*popt))
    y_fit = expo(tdata,*popt)
    # Plot the fit for RFP
    plt.plot(tdata,y_fit,c='tab:red',linestyle='dashed',label='RFP-expo')
    # Matplotlib label stuff
    plt.legend()
    # Set y-axis limits to match the original data
    ymin = min(df.GFP.min(),df.RFP.min())
    ymax = max(df.GFP.max(),df.RFP.max())
    yrange = ymax - ymin
    plt.ylim(ymin - 0.1*yrange, ymax + 0.1*yrange)
    plt.xlabel('Time (days)')
    if fc:
        plt.ylabel('Fold Change')
        figname='../figures/'+e_set+'/Expofit/fc/'+Title+'-Nvst.svg'
    else:
        plt.ylabel('Cell count')
        figname='../figures/'+e_set+'/Expofit/'+Title+'-Nvst.svg'
    plt.title(Title)
    plt.tight_layout()
    plt.savefig(figname)
    plt.close(fig) 

# Get a dataframe for doubling time over time
def df_td(df,Title,e_set):
    dt = df['t'].diff().values[1:]
    t = df['t'].rolling(2, min_periods=1).mean()[1:]
    fc = np.log2(df[['GFP','RFP']]+1).diff().values[1:]
    t_d = np.divide(dt,fc.T).T
    df_td = pd.DataFrame(t)
    df_td[['GFP','RFP']] = t_d
    filename='../analysed_data/'+e_set+'/'+Title+'-t_d.csv'
    df_td.to_csv(filename)
    return df_td

# Plot the Doubling Time (growth rate) vs Time
def plot_td(df,Title,e_set):
    fig=plt.figure(figsize=(15,10))
    # Plot 
    plt.plot(df['t'],df['GFP'],c='tab:green',label='GFP')
    plt.plot(df['t'],df['RFP'],c='tab:red',label='RFP')
    # Matplotlib label stuff
    plt.legend()
    plt.xlabel('Time (days)')
    plt.ylabel('Doubling time (days)')
    figname='../figures/'+e_set+'/doublingtime/'+Title+'-t_d.svg'
    plt.title(Title)
    plt.tight_layout()
    plt.savefig(figname)
    plt.close(fig) 