import numpy as np

class Hydrogen_atom:
     def __init__(self, dimension):
        self.dimension = dimension

     def trial_wave_function(self,alpha, r):
        """
         parametrised (trial)wave function of a quantum system

         Parameters
         ----------
         alpha:                                                                      
            variable input, variable input, is being changed to find the minimal 
            energy          
         R: int
            variable input, distance between proton and electron 

         Results
         -------   
         np.exp(- alpha * R): function with two variables
        """
        r = np.linalg.norm(r, axis = 0)
        trial_wave = np.exp(- alpha * r)
        return(trial_wave)

     def E_loc(self, alpha, r):
        """
         Local energy is a function that depends on the positions of the particles
         and alpha. It is constant if ψT is the exact eigenfunction of 
         the Hamiltonian.
         Parameters
         ----------
         alpha: int
             variable input, is being changed to find the minimal energy
         R: int
            variable input, distance between proton and electron 
         Results
         -------
         E_loc: function with two variables
        """
        r = np.linalg.norm(r, axis = 0)
        trial_wave = -1/r-alpha*(alpha-2/r)/2
        return(trial_wave)

     def der_ln_twf(self, alpha, r):
        """alpha derivative of the natural logarithm of the trial wave function, 
         needed to calculate the alpha derivative of the energy
         Parameters
         ----------
         R: int
             variable input, distance between proton and electron
    
         Results
         -------
         -R: function with one variable
        """
        return(-np.linalg.norm(r, axis = 0))
