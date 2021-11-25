import numpy as np
import astropy.io.fits as pf
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import importlib
import scipy.stats as ss
from scipy.optimize import curve_fit
from kapteyn import kmpfit

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

data = pf.getdata('Simple_mass_metallicity_210927.fits', 1)
x_all = data['mass'].astype('float64')
y_all = data['OH'].astype('float64')

def residual(p, data):
    x, y = data
    a, b, c = p
    return(y-(a*x**2+b*x+c))

fitobj = kmpfit.Fitter(residuals=residual, data=(x_all, y_all))
parinit = [-1, 0, 9]
fitobj.fit(params0 = parinit)
optpar = fitobj.params
print("fit result : %0.2fx^2 + %0.2fx + %0.2f" % (optpar[0], optpar[1], optpar[2]))
print("kmpfit chi2_min : %0.2f" % fitobj.chi2_min)
print("kmpfit reduced chi2 : %0.2f" % fitobj.rchi2_min)
print("kmpfit NDF : %0.2f" % fitobj.dof)
print("chi2/NDF : %0.2f" %(fitobj.rchi2_min/fitobj.dof))

