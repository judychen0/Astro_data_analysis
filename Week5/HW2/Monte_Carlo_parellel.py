import numpy as np
import sys
import os.path

mean = 0
sigma  = 10

isim = int(sys.argv[1])
simvar = 0

npoints = 100
xaxis = np.zeros(npoints)
var = np.zeros(npoints)
theo_var2 = np.zeros(npoints)

filename = "sim_"+str(isim)
save_path = "/home/jou/astro/sim_output_txt"
full_filename = os.path.join(save_path, filename+".txt")
fp = open(full_filename, "w")

for ipoint in range(0, npoints):
    ndata = (ipoint+1)*1000
    xaxis[ipoint] = ndata

    randomdata = np.random.normal(mean, sigma, ndata)
    simvar = np.var(randomdata)

    var[ipoint] = simvar
    theo_var2[ipoint] = 2*pow(sigma, 4)/ndata

    write_array = []
    write_array.append(str(var[ipoint])+"\n")
    fp.writelines(write_array)

fp.close()

#print(var)
#print(theo_var2)
#run commandline
#/usr/bin/time parallel --progress --jobs 20 'python3 Monte_Carlo_parellel.py' ::: {0..1000}



