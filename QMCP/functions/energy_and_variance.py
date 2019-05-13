import numpy as np
from QMCP.functions import one_d_metropolis, three_d_metropolis, six_d_metropolis
from QMCP.functions import bootstrap

def expectation_value(E_loc):
    print(E_loc,'E_loc')
    E = (1/len(E_loc))*np.sum(E_loc)
    return(E)

def variance(E_loc):
    var = (1/len(E_loc))*np.sum(E_loc**2) - ((1/len(E_loc))*np.sum(E_loc))**2
    return(var)

def vmc(alpha, quantum_system):

    E_ground = np.zeros(len(alpha))
    E_ground_error = np.zeros(len(alpha))
    var = np.zeros(len(alpha))
    for i in range(len(alpha)):

        f = lambda R: quantum_system.trial_wave_function(alpha[i],R)
        if quantum_system.dimension == 1: 
            prob_dens = one_d_metropolis(f,30000,400)   
        elif quantum_system.dimension == 3:
            prob_dens = three_d_metropolis(f,30000,400)
        else:
            prob_dens = six_d_metropolis(f,30000,400)
            
        E = quantum_system.E_loc(alpha[i], prob_dens)
        E_ground_error[i] = bootstrap(E[0:1000],100)
        E_ground[i] = expectation_value(E)
        var[i] = variance(E)

    return(E_ground, E_ground_error, var)



