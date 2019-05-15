import numpy as np
from QMCP.functions import metropolis
from QMCP.functions import bootstrap

def vmc(alpha, quantum_system, N, n_walkers):

    E_ground = np.zeros(len(alpha))
    E_ground_error = np.zeros(len(alpha))
    var = np.zeros(len(alpha))
    var_error = np.zeros(len(alpha))
    for i in range(len(alpha)):

        f = lambda R: quantum_system.trial_wave_function(alpha[i],R)
        prob_dens = metropolis(f,N,n_walkers,quantum_system.dimension)
        E = quantum_system.E_loc(alpha[i], prob_dens)

        E_ground_error[i], var[i], var_error[i] = bootstrap(E,15000)
        E_ground[i] = np.mean(E)
        
    return(E_ground, E_ground_error, var, var_error)



