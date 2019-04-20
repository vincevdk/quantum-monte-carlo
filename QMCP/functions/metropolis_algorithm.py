import numpy as np
import matplotlib.pyplot as plt

def metropolis(function, N, n_walkers = 1):

    x = np.zeros((N, n_walkers))    
    x[0] = 3 * np.random.rand(n_walkers)
    h = 1/10
    t = 0
    
    for i in range(len(x)):
        x_trial = np.random.uniform(-h/2, h/2, n_walkers)

        x_trial = x[i-1] + x_trial

        r = (function(x_trial)/function(x[i-1]))**2
        
        eta = np.random.uniform(0,1,size = n_walkers) 
        
        x[i] = np.where(r >= 1, x_trial, (np.where(eta < r, x_trial, x[i-1])))

    return(x)



