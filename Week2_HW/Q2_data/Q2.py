import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf

def my_plot_style():
   
    params = {'legend.fontsize': 20,
             'axes.labelsize': 20,
             'axes.titlesize':20,
             'xtick.labelsize':16,
             'ytick.labelsize':16,
             'xtick.major.size':5,
              'xtick.minor.size':2.5,
             'ytick.major.size':5,
              'ytick.minor.size':2.5,
             'figure.facecolor':'w',
             #'lines.linewidth' : 1.5,
              'xtick.major.width':1.5,
              'ytick.major.width':1.5,
              'xtick.minor.width':1.5,
              'ytick.minor.width':1.5,
              'xtick.major.pad': 12,
              'ytick.major.pad': 8,
              'axes.linewidth':1.5,
              'xtick.direction':'in',
              'ytick.direction':'in',
             'ytick.labelleft':True,
              'text.usetex' : False,
             'font.family': 'sans-serif'}
  
    plt.rcParams.update(params)

data = pf.open('Simple_mass_metallicity_210927.fits')
catalog = data[1].data

my_plot_style()

plt.figure(figsize = (8, 8))
plt.hist2d(catalog['mass'], catalog['OH'], bins = [100, 100], range = [[8, 12], [8, 9.5]], cmap = plt.cm.BuPu)
#plt.colorbar()
cbar = plt.colorbar()
cbar.ax.get_yaxis().labelpad = 18
cbar.ax.tick_params(labelsize=15) 
cbar.ax.set_ylabel('counts', rotation=270)
plt.xlabel(r'Log(M$_{*}$/M$_{\odot})$')
plt.ylabel('Log(O/H)+12')
plt.subplots_adjust(bottom = 0.15, top = 0.9, left = 0.15, right = 0.98)
plt.show()
