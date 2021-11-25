import os
import os.path
import string
import sys
import numpy as np

#nfile = os.popen("ls | wc -l").read()
nsim = int(os.popen("ls | wc -l").read())
npoints = 100

#input_string = str(sys.argv[1])
#split_input = input_string.split(".")[0].split("_")[1]

#print(split_input)
#isim = int(split_input)
filename = "simresults"
save_path = "/home/jou/astro"
full_filename = os.path.join(save_path, filename+".txt")
fp = open(full_filename, "w")
write_array = []

open_path = "/home/jou/astro/sim_output_txt/"
os.chdir(open_path)
var2 = np.zeros(npoints)


#openfilename  = input_string
#full_openfilename = os.path.join(open_path, openfilename)
for ipoint in range(0, npoints):
    npsimvar = np.zeros(nsim)
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            file_path = os.path.join(open_path, file)
            # call read text file function
            with open(file_path, "r") as read:
                lines = read.readlines()[0]
                simvar = lines.split(" ")[0]
                np.append(npsimvar, simvar)
    var2[ipoint] = np.var(npsimvar)
    write_array.append(str(var2[ipoint])+" ")

fp.writelines(write_array)
fp.close()
          



    
