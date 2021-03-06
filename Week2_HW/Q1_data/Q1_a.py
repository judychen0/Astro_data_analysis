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

data = pf.open('a_catalog_with_50_objects.fits')
catalog = data[1].data
SDSS_u = catalog['SDSS_u']
SDSS_z = catalog['SDSS_z']
UmZ = np.subtract(SDSS_u, SDSS_z)

my_plot_style()

plt.figure(figsize = (8, 8))
plt.hist2d(SDSS_z, UmZ, bins=[60, 80], range=[[17, 20], [-1, 1]], cmap=plt.cm.BuPu)
plt.colorbar()
plt.xlabel('SDSS_z')
plt.ylabel('SDSS_u - SDSS_z')
plt.subplots_adjust(bottom = 0.1, top = 0.9, left = 0.15, right = 0.98)
plt.show()

