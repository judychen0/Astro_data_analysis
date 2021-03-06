import astropy.io.fits as pf
import numpy as np
import matplotlib.pyplot as plt
from kapteyn import kmpfit
from scipy.optimize import curve_fit
import math

black_body = pf.getdata('spec-3744-55209-0386.fits',1)
search = np.where(black_body['ivar']>0)

flux = black_body['flux'][search[0]].astype('float64')
wavelength = 10**black_body['loglam'][search[0]].astype('float64')
wavelength_u = wavelength/1000
ivar = black_body['ivar'][search[0]].astype('float64')

def blackbody_fit(x, a, b):
    return a/pow(x,5)/(math.exp(b/x)-1)

popt, pcov = curve_fit(blackbody_fit, wavelength, flux)
