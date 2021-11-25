import numpy as np
import astropy.io.fits as pf
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import importlib
import scipy.stats as ss
from scipy.optimize import curve_fit
from kapteyn import kmpfit
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


data = pf.getdata('spec-3744-55209-0386.fits',1)
search = np.where(data['ivar']>0)

flux = data['flux'][search[0]].astype('float64')
wavelength = (10**data['loglam'][search[0]].astype('float64'))
#wavelength_u = wavelength/1000
ivar = data['ivar'][search[0]].astype('float64')

def residual(p, data):
    x, y, yerr = data
    amp, temp = p
    hc = 1.98/10**25
    k = 1.38/10**23
    c = 3*10**8
    wavel = x/10**10
    exp = np.exp(hc/(wavel*k*temp))
    model = amp*(hc*c/wavel**5)*(1/exp-1)/10**17
    return (np.sqrt(yerr))*(y-(model))

fitobj = kmpfit.Fitter(residuals=residual, data=(wavelength, flux, ivar))
parinit = [10**5, 9800]
fitobj.fit(params0=parinit)
amp = fitobj.params[0]
temp = fitobj.params[1]
print("fit temparature : %0.2f" %temp)
print("kmpfit reduced chi2 : %0.2f" % fitobj.rchi2_min)
