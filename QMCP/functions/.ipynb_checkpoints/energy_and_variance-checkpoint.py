import numpy as np
from QMCP.functions import metropolis
from QMCP.functions import bootstrap

def vmc(alpha, quantum_system, N, n_walkers):
    """" This function calculates the ground state energy, variance, 
    error of the ground state energy and error of the variance.
    
    Parameters:
    ------------
    alpha: array 
        can be any size
    quantum_system: class with properties dimensions
        modules: trial_wave_function, E_loc, der_ln_twf
    N: int
    n_walkers: int
    
    Results:
    ---------
    E_ground: array of size len(alpha)
    E_ground_error: array of size len(alpha)
    var: array of size len(alpha)
    var_error: array of size len(alpha)
    """

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
        print(E_ground[i], 'E_ground')
        
    return(E_ground, E_ground_error, var, var_error)



