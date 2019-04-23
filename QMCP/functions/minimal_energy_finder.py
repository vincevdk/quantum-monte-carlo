import numpy as np
from QMCP.functions import one_d_metropolis

def expectation_value(E_loc):
    E = (1/len(E_loc))*np.sum(E_loc)
    return(E)

def derivative_E(alpha,function, E_loc):
    f = lambda R: function(R,alpha)
    prob_dens = metropolis(f,10000)
    E = E_loc(alpha, prob_dens)
    E_ground = expectation_value(E)
    deriv_E = 2*(expectation_value(-E*prob_dens**2) - E_ground*expectation_value(-prob_dens**2))
    return(deriv_E, E_ground)

def minimization_alpha(trial_function, E_loc):
    gamma = 0.1
    tol = 0.00001
    max_it = 1000
    alpha_min = 1.2
    difference = 1.2
    i = 0
    E_ground = []
    alpha_array = []
    alpha_array.append(alpha_min)

    while abs(difference) >= tol and i < max_it:
        keep = alpha_min
        der_E, E_ground = derivative_E(alpha_min,trial_function, E_loc)
        alpha_min = alpha_min - gamma * der_E
        alpha_array.append(alpha_min)
        difference = alpha_min - keep
        print(alpha_min, 'alpha')
        i += 1

    print("minimum alpha = ", alpha_min)
    return(alpha_array)
