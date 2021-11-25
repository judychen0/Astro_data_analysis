import numpy as np
import matplotlib.pyplot as plt

new_data = np.load("simple_correlation_1000_x_y.npy")
x = new_data[0,:]
y = new_data[1,:]


def y_mean(x, y, atx):
    y_search = np.where(x==atx)
    y_mean = np.mean(y[y_search[0]])

    return y_mean

mean_y_0 = y_mean(x, y, 0)
print("mean_y_0 mean : "+str(mean_y_0))
mean_y_1 = y_mean(x, y, 1)
print("y_1 mean : "+str(mean_y_1))

dy = mean_y_1 - mean_y_0
print("dy : "+str(dy))

def y_err(x, y, atx):
    y_search = np.where(x==atx)[0]
    y_std = np.std(y[y_search])
    y_err = y_std/np.sqrt(len(y_search))
    
    return y_err

err_y_0 = y_err(x, y, 0)
err_y_1 = y_err(x, y, 1)
err_dy = np.sqrt(err_y_0**2+err_y_1**2)

print("dy error : "+str(err_dy))
print("dy = "+str(dy)+" +- "+str(err_dy))

bootstrap_time = 200
bootstrap_dy = np.zeros(bootstrap_time)

for iboot in range(0, bootstrap_time):
    random_x = np.random.randint(0, len(x), len(x))
    random_y = np.random.randint(0, len(y), len(y))

    new_random_x = x[random_x]
    new_random_y = y[random_y]

    mean_y_0 = y_mean(new_random_x, new_random_y, 0)
    mean_y_1 = y_mean(new_random_x, new_random_y, 1)
    
    bootstrap_dy[iboot] = mean_y_1 - mean_y_0

bperr_dy = np.std(bootstrap_dy)
print("Bootstrap error of dy : "+str(bperr_dy))
