import numpy as np
from QMCP.functions import metropolis

def variance(E_loc):
    var = (1/10000)*np.sum(E_loc**2) - ((1/10000)*np.sum(E_loc))**2
    return(var)

def vmc(alpha, trial_function, E_loc_func):
    E_loc = np.zeros([10000,len(alpha)])
    E = np.zeros(len(alpha))
    var = np.zeros(len(alpha))
    for i in range(len(alpha)):

        f = lambda R: trial_function(R,alpha[i])
        prob_dens = metropolis(f,10000)
        E_loc[:,i] = E_loc_func(alpha[i], prob_dens)
        E[i] = np.sum(E_loc[:,i])/10000
        var[i] = variance(E_loc[:,i])
        
    return(E, var)
