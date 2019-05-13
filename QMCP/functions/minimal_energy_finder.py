import numpy as np
from QMCP.functions import one_d_metropolis, three_d_metropolis, six_d_metropolis

def expectation_value(E_loc):
    E = (1/len(E_loc))*np.sum(E_loc)
    return(E)

def derivative_E(alpha, quantum_system):
    f = lambda R: quantum_system.trial_wave_function(alpha, R)
    if quantum_system.dimension == 1:
        prob_dens = one_d_metropolis(f,30000,400)

    elif quantum_system.dimension == 3:
        prob_dens = three_d_metropolis(f,30000,400)

    else:
        prob_dens =six_d_metropolis(f,30000,400)

    E = quantum_system.E_loc(alpha, prob_dens)
    E_ground = expectation_value(E)
    deriv_E = 2*(expectation_value(E*quantum_system.der_ln_twf(alpha, prob_dens) - E_ground*expectation_value(quantum_system.der_ln_twf(alpha,prob_dens))))
    return(deriv_E, E_ground)

def minimization_alpha(quantum_system):
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

    gamma = 0.1
    tol = 0.0001
    max_it = 1000
    alpha_min = 0.20
    difference = 1.2
    i = 0
    E_ground = []
    alpha_array = []
    alpha_array.append(alpha_min)

    while abs(difference) >= tol and i < max_it:
        keep = alpha_min
        der_E, E_ground = derivative_E(alpha_min, quantum_system)
        alpha_min = alpha_min - gamma * der_E
        alpha_array.append(alpha_min)
        difference = alpha_min - keep
        print(alpha_min, 'alpha')
        i += 1

    print("minimum alpha = ", alpha_min)
    return(alpha_array)
