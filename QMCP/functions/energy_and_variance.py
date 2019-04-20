import numpy as np
from QMCP.functions import metropolis

def expectation_value(E_loc):
    E = (1/len(E_loc))*np.sum(E_loc)
    return(E)

def variance(E_loc):
    var = (1/100000)*np.sum(E_loc**2) - ((1/100000)*np.sum(E_loc))**2
    return(var)

def vmc(alpha, trial_function, E_loc):

    E_ground = np.zeros(len(alpha))
    var = np.zeros(len(alpha))
    for i in range(len(alpha)):

        f = lambda R: trial_function(alpha[i],R)
        prob_dens = metropolis(f,100000)
        E = E_loc(alpha[i], prob_dens)
        E_ground[i] = expectation_value(E)
        var[i] = variance(E)
        
    return(E_ground, var)
