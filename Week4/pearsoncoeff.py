import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import scipy.stats as ss

def pearson_correlation(par1, par2):
    std1 = np.std(par1)
    std2 = np.std(par2)
    mean1 = np.mean(par1)
    mean2 = np.mean(par2)

    ndata = len(par1)
    cov = (1/ndata)*(np.sum((par1-mean1)*(par2-mean2)))
    rho = cov/(std1*std2)
    return rho

data = pf.open('sky_maps_new_64_v6.fits')
ISM = data[1].data
EBV = ISM['SFD']
HI = ISM['HI']/1e21

conversion_factor = 2*1e20/1e21
H2 = ISM['CO10']*conversion_factor

EBV_HI_pearson_m = pearson_correlation(EBV, HI)
print(pearson_correlation(EBV, HI))
print(round(ss.pearsonr(EBV, HI)[0], 2))
pearson_correlation(EBV, H2)
print(ss.pearsonr(EBV, H2))
                     
        
