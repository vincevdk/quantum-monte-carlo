import numpy as np
import matplotlib.pyplot as plt

def metropolis(function, N, n_walkers = 1, integral_range = None):

    x = np.zeros((N, n_walkers))
    x[0] = 3 * np.random.rand(n_walkers)
    h = 1/10
    t = 0
    if integral_range != None:
        x[0] = np.where(x[0] <= 0, -x[0]+0.1, x[0])
 
    for i in range(len(x)):
        x_trial = np.random.uniform(-h/2, h/2, n_walkers)

        x_trial = x[i-1] + x_trial

        r = (function(x_trial)/function(x[i-1]))**2
        
        eta = np.random.uniform(0,1,size = n_walkers) 
        
        x[i] = np.where(r >= 1, x_trial, (np.where(eta < r, x_trial, x[i-1])))
        if integral_range !=None:
            x[i] = np.where(x[i]<=0 , -x[0]+0.1, x[0])

    x = np.reshape(x[4000:], n_walkers*N - (n_walkers * 4000))
    return(x)





