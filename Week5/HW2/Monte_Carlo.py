import numpy as np
import matplotlib.pyplot as plt
import sys
import os.path

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

    
mean = 0
sigma = 10

nsim = 1000
simvar = np.zeros(nsim)

npoints = 100
xaxis = np.zeros(npoints)
var2 = np.zeros(npoints)
theo_var2 = np.zeros(npoints)

#filename = "sim_noparallel"
#save_path = "/home/jou/astro"
#full_filename = os.path.join(save_path, filename+".txt")
#fp = open(full_filename, "w")
write_array = []

for ipoint in range(0, npoints):
    ndata = (ipoint+1)*1000
    xaxis[ipoint] = ndata
    
    for isim in range(0, nsim):
        randomdata = np.random.normal(mean, sigma, ndata)
        simvar[isim] = np.var(randomdata)

    var2[ipoint] = np.var(simvar)
    theo_var2[ipoint] = 2*pow(sigma, 4)/ndata

    #write_array = []
    #write_array.append(str(ipoint)+"point "+str(var2[ipoint])+" "+str(theo_var2[ipoint])+"\n")
    #fp.writelines(write_array)
    print(f"Write {ipoint+1} line")

#print(var2)
#print(theo_var2)


my_plot_style()
plt.figure(figsize = (8, 8))
plt.scatter(xaxis, var2, s=15, c="#67ccc1", label="My simulation")
plt.scatter(xaxis, theo_var2, s=15, c="#ff3360", label="Theoretical calculation")
plt.legend()
plt.xlabel("N data point")
plt.ylabel("Var of Var")
plt.show()

