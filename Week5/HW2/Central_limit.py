import numpy as np
import matplotlib.pyplot as plt
import math

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
    

nsim = 1000
simmean = np.zeros(nsim)
simgauss = np.zeros(nsim)

npoints = 40
xaxis = np.zeros(npoints)
std = np.zeros(npoints)
gstd = np.zeros(npoints)
mean_precision = np.zeros(npoints)
gmean_precision = np.zeros(npoints)

for ipoint in range(0, npoints):
    ndata = (ipoint+1)*1000
    xaxis[ipoint] = ndata

    for isim in range(0, nsim):
        randomdata = np.random.standard_cauchy(ndata)
        simmean[isim] = np.mean(randomdata)

        randomgauss = np.random.normal(0, 1, ndata)
        simgauss[isim] = np.mean(randomgauss)
        
    std[ipoint] = np.std(simmean)
    mean_precision[ipoint] = std[ipoint]/math.sqrt(ndata)
    gstd[ipoint] = np.std(simgauss)
    gmean_precision[ipoint] = gstd[ipoint]/math.sqrt(ndata)
    print(f"Write {ipoint+1} line")
print(gmean_precision)
    
#print(mean_precision)
my_plot_style()
plt.figure(figsize = (8, 8))
plt.scatter(xaxis, mean_precision, s=15, c="#67ccc1", label="Cauchy distribution")
plt.scatter(xaxis, gmean_precision, s=15, c="#ff3360", label="Gaussain distribution")
plt.legend()
plt.yscale("log")
ax = plt.gca()
ax.set_ylim([0.00001, 10])
plt.xlabel("N data point")
plt.ylabel(r'$\sigma$/$\sqrt{N}$')
plt.show()
