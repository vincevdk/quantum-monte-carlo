import numpy as np
from QMCP.functions import metropolis


def derivative_E(alpha, quantum_system, N, n_walkers):
    f = lambda R: quantum_system.trial_wave_function(alpha, R)
    prob_dens = metropolis(f,N,n_walkers, quantum_system.dimension)
    E = quantum_system.E_loc(alpha, prob_dens)

    E_ground = np.mean(E)
    deriv_E = 2*(np.mean(E*quantum_system.der_ln_twf(alpha, prob_dens) - E_ground*np.mean(quantum_system.der_ln_twf(alpha,prob_dens))))
    return(deriv_E, E_ground)

def minimization_alpha(quantum_system, N, n_walkers):
    """
    Finds the alpha for which the local energy is minimal, using a simple 
    damped steepest decent method.
    Parameters
    ----------
    trial_function: function 
        parametrised (trial)wave function of a quantum system 
    E_loc: function
        Local energy is a function that depends on the positions of the particles
        and alpha
    der_ln_twf: function
        alpha derivative of the natural logarithm of the trial wave function,    
        needed to calculate the alpha derivative of the energy 
    dimension: int
        

    Results
    -------
    alpha_array: array of size i
        contains the alpha at each itteration
         
    """

    gamma = 0.5
    tol = 0.001
    max_it = 1000
    alpha_min = 1.2
    difference = 1.2
    i = 0
    E_ground = []
    alpha_array = []
    alpha_array.append(alpha_min)

    while abs(difference) >= tol and i < max_it:
        keep = alpha_min
        der_E, E_ground = derivative_E(alpha_min, quantum_system, N, n_walkers)
        alpha_min = alpha_min - gamma * der_E
        alpha_array.append(alpha_min)
        difference = alpha_min - keep
        i += 1
        print(alpha_min, "alpha")

    print("minimum alpha = ", alpha_min)
    return(alpha_array)
