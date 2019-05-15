import numpy as np

class Oscillator:
    def __init__(self, dimension):
        self.dimension = dimension
        

    def trial_wave_function(self, alpha, R):
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

    def E_loc(self,alpha, R):
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
        E_loc = (alpha + (R**2)*(0.5 - 2*alpha**2))
        E_loc = np.reshape(E_loc, E_loc.shape[1])
        return(E_loc)

    def der_ln_twf(self,alpha,R):
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
        return(-np.power(R,2))
