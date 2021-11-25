import matplotlib.pyplot as plt
import numpy as np

mu = 1
sigma = 1
std = np.zeros(100)
for ipoint in range(0, 100):
    ndata = (ipoint+1)*100
    mean = np.zeros(ndata)
    for isim in range(1, 1000):
        randomdata = np.random.normal(mu, sigma, ndata)
        mean[isim] = np.mean(randomdata)

    std.append(np.std(mean)/np.sqrt(ndata))

    
    
