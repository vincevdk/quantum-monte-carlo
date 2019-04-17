
import numpy as np
import matplotlib.pyplot as plt
from metropolis_algorithm import metropolis

## variational quantum monte carlo simulation
## initialize

N = 10000

def trial_wave_function(R, alpha):
    return(np.exp(- alpha * R**2))

def expectation_value(E_loc):
    E = (1/N)*np.sum(E_loc)
    return(E)

def variance(E_loc):
    var = (1/N)*np.sum(E_loc**2) - ((1/N)*np.sum(E_loc))**2
    return(var)

def derivative_E(alpha,function):

    f = lambda R: function(R,alpha)
    prob_dens = metropolis(f,10000)
    E_loc = alpha + (prob_dens**2)*(0.5-2*alpha**2)
    E_ground = expectation_value(E_loc)
    deriv_E = 2*(expectation_value(-E_loc*prob_dens**2) - E_ground*expectation_value(-prob_dens**2))

    return(deriv_E, E_ground)

def minimization_alpha(function):
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
        der_E, E_ground = derivative_E(alpha_min,function)  
        alpha_min = alpha_min - gamma * der_E
        alpha_array.append(alpha_min)
        difference = alpha_min - keep
        print(alpha_min, 'alpha')
        i += 1

    print("minimum alpha = ", alpha_min)
    return(alpha_array)

alpha = minimization_alpha(trial_wave_function)
_ = np.linspace(0,len(alpha),len(alpha))
plt.title('minimization of alpha')
plt.plot(_,alpha, 'ro')

plt.show()
