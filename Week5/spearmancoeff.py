import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import scipy.stats as ss
from scipy.stats import rankdata

def pearson_correlation(par1, par2):
    std1 = np.std(par1)
    std2 = np.std(par2)
    mean1 = np.mean(par1)
    mean2 = np.mean(par2)

    ndata = len(par1)
    cov = (1/ndata)*(np.sum((par1-mean1)*(par2-mean2)))
    rho = cov/(std1*std2)
    return rho

def spearman_correlation(par1, par2):
    rank_par1 = len(par1) - rankdata(par1).astype(int) +1
    rank_par2 = len(par2) - rankdata(par2).astype(int) +1
    
    std1 = np.std(rank_par1)
    std2 = np.std(rank_par2)
    mean1 = np.mean(rank_par1)
    mean2 = np.mean(rank_par2)

    ndata = len(rank_par1)
    cov = (1/ndata)*(np.sum((rank_par1-mean1)*(rank_par2-mean2)))
    rho = cov/(std1*std2)
    return rho

data = pf.open('sky_maps_new_64_v6.fits')
ISM = data[1].data
EBV = ISM['SFD']
HI = ISM['HI']/1e21

conversion_factor = 2*1e20/1e21
H2 = ISM['CO10']*conversion_factor

rank_EBV = len(EBV) - rankdata(EBV).astype(int) +1
rank_HI = len(HI) - rankdata(HI).astype(int) +1

mypearson = pearson_correlation(rank_EBV, rank_HI)
outstring = "my spearson coeff :"
#print(ss.pearsonr(rank_EBV, rank_HI))
#print(mypearson)

myspearman = spearman_correlation(EBV, HI)
print(ss.spearmanr(EBV, HI))
print(myspearman)


