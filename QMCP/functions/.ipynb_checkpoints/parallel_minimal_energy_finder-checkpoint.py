from __future__ import print_function
from random import random
import multiprocessing
import datetime
import numpy as np
from QMCP.functions import one_d_metropolis, three_d_metropolis

def expectation_value(E_loc):
    E = (1/len(E_loc))*np.sum(E_loc)
    return(E)

def derivative_E(alpha, quantum_system):
    f = lambda R: quantum_system.trial_wave_function(alpha, R)
    if quantum_system.dimension == 1:
        prob_dens = one_d_metropolis(f,50000,400)
    else:
        prob_dens = three_d_metropolis(f,50000,400)

    E = quantum_system.E_loc(alpha, prob_dens)
    E_ground = expectation_value(E)
    deriv_E = 2*(expectation_value(E*quantum_system.der_ln_twf(prob_dens) - E_ground*expectation_value(quantum_system.der_ln_twf(prob_dens))))
    return(deriv_E, E_ground)

class WorkerProcess(multiprocessing.Process):

    def __init__(self, args):
        multiprocessing.Process.__init__( self, args=args )
        self.quantum_system = args[0]
        self.alpha = args[1]
        self.q = args[2]

    def run(self):
        self.q.put(minimization_alpha(self.quantum_system, self.alpha))

def minimization_alpha(quantum_system, alpha_min):
    gamma = 0.1

    keep = alpha_min
    der_E, E_ground = derivative_E(alpha_min, quantum_system)
    alpha_min = alpha_min - gamma * der_E

    difference = alpha_min - keep
    return(alpha_min, difference)

def parallel_minimization_alpha(quantum_system):
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
    tol = 0.0001
    max_it = 10000
    difference = 1.2
    j = 0
    E_ground = []
    minimal_alpha_array = np.array([])
    num_p = 3 
    jobs = []
    q = multiprocessing.Queue()
    alpha = 1.2
    dif = 1.2

    alpha,dif = minimization_alpha(quantum_system, alpha)

    differences = np.zeros((3))
    alpha_results = np.zeros((3))
#    alphas_to_be_calculated = np.array([alpha-0.5, alpha, alpha+0.5])
    
    minimal_alpha_array = np.append(minimal_alpha_array,alpha)

    while abs(dif) >= tol and j < max_it:

        alphas_to_be_calculated = [alpha, alpha+dif,alpha+2*dif]

        for i in range(num_p):
            pro = WorkerProcess( args=(quantum_system, alphas_to_be_calculated[i], q) )
            pro.start()
            jobs.append(pro)

        for i in range( num_p ):
            alpha_results[i], differences[i] = q.get()

        print(alpha_results, 'alpha results')
        print(differences,'differences')
        indice_minimum = np.argmin(abs(differences))
        dif = differences[indice_minimum]
        alpha = alpha_results[indice_minimum]
       

        
        minimal_alpha_array = np.append(minimal_alpha_array,alpha)
        j += 1
        print(minimal_alpha_array, 'minimal_alpha_array')
    return(minimal_alpha_array)

    
