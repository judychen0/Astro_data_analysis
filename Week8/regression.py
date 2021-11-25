import astropy.io.fits as pf
import numpy as np
import matplotlib.pyplot as plt
from kapteyn import kmpfit

data = pf.getdata('Simple_mass_metallicity_210927.fits', 1)
x_all = data['mass'].astype('float64')
y_all = data['OH'].astype('float64')
    
def residual(p, data):
    x, y = data
    a, b, c = p
    model = a+b*x+c*x*x
    return(y-model)

fitter = kmpfit.Fitter(residual, data=(x_all, y_all))
paramsinit = [-2,2,1]
fitter.fit(params0 = paramsinit)

print("fit param0 = %0.2f" % fitter.params[0])
print("fit param1 = %0.2f" % fitter.params[1])
print("fit param2 = %0.2f" % fitter.params[2])
chi2 = fitter.chi2_min
NDF = fitter.dof
#chi2_NDF = chi2/NDF
print("chi2 %0.2f" % chi2)
print("NDF %0.2f" % NDF)
