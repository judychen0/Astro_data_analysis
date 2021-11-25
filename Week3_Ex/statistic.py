import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as pf
import numpy as np
import scipy.stats as ss
import statistics 

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

data = pf.open('SDSS_QSO_spectra_short.fits')
spectra = data[0].data
inv = data[1].data
wavelength = data[2].data
npixel = 3010
nonj = 1000

mean_spec = np.zeros((npixel))
median_spec = np.zeros(npixel)
sigmaclip_spec = np.zeros(npixel)
inv_spec = np.zeros(npixel)
geomean_spec = np.zeros(npixel)

for ipix in range(0, npixel):
    mean_spec[ipix] = np.mean(spectra[:, ipix])
    median_spec[ipix] = np.median(spectra[:, ipix]);
    sigmaclip_spec[ipix] = np.mean(ss.sigmaclip(spectra[:, ipix], low = 5, high = 5)[0])
    inv_spec[ipix] = np.sum(spectra[:, ipix] * inv[:, ipix])/np.sum(inv[:, ipix])
    positive = np.where(spectra[:,ipix]>0)[0]
    geomean_spec[ipix] = ss.mstats.gmean(spectra[positive, ipix])

my_plot_style()

plt.figure(figsize=(15,45))
plt.subplot(6, 1, 1)
plt.plot(wavelength, mean_spec, c = '#b23b8c', label = 'mean')

plt.subplot(6, 1, 2)
plt.plot(wavelength, median_spec, c = '#ffea00', label = 'median')

plt.subplot(6, 1, 3)
plt.plot(wavelength, sigmaclip_spec, c = '#03a9f4', label = 'sigma clip')

plt.subplot(6, 1, 4)
plt.plot(wavelength, inv_spec, c = '#ff9e00', label = 'inverse Var weight')

plt.subplot(6, 1, 5)
plt.plot(wavelength, geomean_spec, c = '#4caf50', label = 'geometric mean')

plt.subplot(6, 1, 6)
#plt.plot(wavelength, mean_spec, c = '#b23b8c')
plt.plot(wavelength, median_spec, c = '#ffea00')
plt.plot(wavelength, sigmaclip_spec, c = '#03a9f4')
plt.plot(wavelength, inv_spec, c = '#ff9e00')
plt.plot(wavelength, geomean_spec, c = '#4caf50')
plt.xlabel('rest frame wavelength [$\\rm \\AA$]',fontsize=20)
plt.legend()
plt.show()
