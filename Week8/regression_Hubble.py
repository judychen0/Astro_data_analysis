import numpy as np
import astropy.io.fits as pf
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import importlib
import scipy.stats as ss
from scipy.optimize import curve_fit
from kapteyn import kmpfit

data = pf.getdata('hubble_original_data.fits',1)
x = data['distance']
y = data['velocity']
print("spearman correlation coeff. : "+str(ss.spearmanr(x,y)[0]))
print("pearson correlation coeff. : "+str(ss.pearsonr(x,y)[0]))

coeff = []
for iboot in range(0, 1000):
    rindex = np.random.randint(0, len(x), len(x))
    coeff.append(ss.pearsonr(x[rindex], y[rindex])[0])

uncertainty = np.std(coeff)
print("uncertainty of bootstrap method for pearson coeff. : "+str(uncertainty))


def linear_curve(x, a, b):
    return a*x+b

popt, pcov = curve_fit(linear_curve, x, y)
slope, yinter = popt
print("fit result : %0.2f*x + %0.2f" %(slope, yinter))

def residual(p, data):
    x, y = data
    a, b = p
    return (y-(a*x+b))


x = data['distance'].astype('float64')
y = data['velocity'].astype('float64')
fitobj = kmpfit.Fitter(residuals=residual, data=(x, y))
parinit = [0, 75]
fitobj.fit(params0=parinit)
kmpslope = fitobj.params[0]
kmpyinter = fitobj.params[1]
print("kmpfit result : %0.2f*x + %0.2f" %(kmpslope, kmpyinter))
print("kmpfit chi2_min : %0.2f" % fitobj.chi2_min)
print("kmpfit reduced chi2 : %0.2f" % fitobj.rchi2_min)
print("kmpfit NDF : %0.2f" % fitobj.dof)
print("chi2/NDF : %0.2f" %(fitobj.rchi2_min/fitobj.dof))

fitslope = []
for iboot in range(0, 1000):
    rindex = np.random.randint(0, len(x), len(x))
    fitobj = kmpfit.Fitter(residuals=residual, data=(x[rindex], y[rindex]))
    fitobj.fit(params0=parinit)
    fitslope.append(fitobj.params[0])

fit_uncertainty = np.std(fitslope)
print("fit slope uncertainty(bootstrap) : %0.2f" % fit_uncertainty)
