import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.harmonic_oscillator import Oscillator

def trial_wave_function(R, alpha):
    """
    parametrised (trial)wave function of a quantum system

    Parameters
    ----------
    R: int
       variable input, position of the oscillator
    alpha: 
       variable input, 
    Results
    -------   
    np.exp(- alpha * R**2): function with two variables
    """
    return(np.exp(- alpha * R**2))

def E_loc(alpha, R):
    """
    Local energy is a function that depends on the positions of the particles
    and alpha. It is constant if ψT is the exact eigenfunction of 
    the Hamiltonian.
    Parameters
    ----------
    alpha: int
       variable input, is being changed to find the minimal energy
    R: int
       variable input, position of the oscillator
    Results
    -------
    E_loc: function with two variables
    """
    return(alpha + (R**2)*(0.5 - 2*alpha**2))

def der_ln_twf(R):
    """alpha derivative of the natural logarithm of the trial wave function, 
    needed to calculate the alpha derivative of the energy
    Parameters
    ----------
    R: int
       variable input, position of the oscillator
    
    Results
    -------
    -R**2: function with one variable
    """
    return(-R**2)


oscillator = Oscillator(1)
alpha = minimization_alpha(oscillator)

steps = np.linspace(0,len(alpha),len(alpha))

plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')
plt.show()
