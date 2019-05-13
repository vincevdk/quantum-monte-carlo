import numpy as np

class Hydrogen_atom:
     def __init__(self, dimension):
        self.dimension = dimension

     def trial_wave_function(self,alpha, R):
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
         return(np.exp(- alpha * R))

     def E_loc(self, alpha, R):
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
         return(-1/R-alpha*(alpha-2/R)/2)

     def der_ln_twf(self, alpha,bR):
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

         return(-R)
