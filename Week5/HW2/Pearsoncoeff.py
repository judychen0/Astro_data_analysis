import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import scipy.stats as ss

data = pf.open('sky_maps_new_64_v6.fits')
ISM = data[1].data
EBV = ISM['SFD']
HI = ISM['HI']/1e21

conversion_factor = 2*1e20/1e21
H2 = ISM['CO10']*conversion_factor

bootstrap_time = 500
Pbootstrap_EBV_HI = np.zeros(bootstrap_time)
Sbootstrap_EBV_HI = np.zeros(bootstrap_time)
Pbootstrap_EBV_H2 = np.zeros(bootstrap_time)
Sbootstrap_EBV_H2 = np.zeros(bootstrap_time)

for iboot in range(0, bootstrap_time):
    random_EBV = np.random.randint(0, len(EBV), len(EBV))
    random_HI = np.random.randint(0, len(HI), len(HI))
    random_H2 = np.random.randint(0, len(H2), len(H2))
    
    new_random_EBV = EBV[random_EBV]
    new_random_HI = HI[random_HI]
    new_random_H2 = H2[random_H2]
    
    Pbootstrap_EBV_HI[iboot] = ss.pearsonr(new_random_EBV, new_random_HI)[0]
    Sbootstrap_EBV_HI[iboot] = ss.spearmanr(new_random_EBV, new_random_HI)[0]
    Pbootstrap_EBV_H2[iboot] = ss.pearsonr(new_random_EBV, new_random_H2)[0]
    Sbootstrap_EBV_H2[iboot] = ss.spearmanr(new_random_EBV, new_random_H2)[0]

Pbperr_EBV_HI = np.std(Pbootstrap_EBV_HI)
Sbperr_EBV_HI = np.std(Sbootstrap_EBV_HI)
Pbperr_EBV_H2 = np.std(Pbootstrap_EBV_H2)
Sbperr_EBV_H2 = np.std(Sbootstrap_EBV_H2)
    
print(f'Pearson(EBV, HI) uncertainty : {Pbperr_EBV_HI:.4f}')
print(f'Spearman(EBV, HI) uncertainty : {Sbperr_EBV_HI:.4f}')
print(f'Pearson(EBV, H2) uncertainty : {Pbperr_EBV_H2:.4f}')
print(f'Spearman(EBV, H2) uncertainty : {Sbperr_EBV_H2:.4f}')


