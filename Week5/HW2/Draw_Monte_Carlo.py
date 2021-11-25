import numpy as np
import matplotlib.pyplot as plt
import sys
import os.path
import string

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

open_path = "/home/judy/Astrophys/Week5/HW2/"
filename = "sim_noparallel"
full_filename = os.path.join(open_path, filename+".txt")

npoints = 100
xaxis = np.zeros(npoints)
var2 = np.zeros(npoints)
theo_var2 = np.zeros(npoints)

for ipoint in range(0, npoints):
    ndata = (ipoint+1)*1000
    xaxis[ipoint] = ndata

with open(full_filename, "r") as read:
    lines = read.readlines()
    ivar2 = []
    itheo_var2 = []
    for l in lines:
        l.replace("\n", " ")
        #print(l.split(" ")[1])
        ivar2.append(l.split(" ")[0])
        itheo_var2.append(l.split(" ")[1])
print(ivar2)
np.append(var2, ivar2)
np.append(theo_var2, itheo_var2)
#print(len(xaxis))
#print(len(var2))

my_plot_style()
plt.figure(figsize = (8, 8))
#plt.scatter(xaxis, var2, s=0.3, c="#67ccc1", label="My simulation")
#plt.scatter(xaxis, theo_var2, s=0.3, c="#ff3360", label="Theoretical calculation")
plt.scatter(xaxis, var2, c="green")
#plt.scatter(xaxis, theo_var2, c="red")
plt.show()
