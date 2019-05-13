import numpy as np

class Helium_atom:
    def __init__(self, dimension):
        self.dimension = dimension
    
    def trial_wave_function(self, alpha, r):
        """
        parametrised (trial)wave function of a quantum system

        Parameters
        ----------
        alpha:                                                                      
            variable input, variable input, is being changed to find the minimal 
            energy          
        r: matrix of shape 6 x N x n_walkers
            N , number of steps
            n_walkers , number of walkers
            :3 x N x n_walkers , distance between proton and electron 1
            3: x N x n_walkers , distance between proton and electron 2

        Results
        -------   
        trial_wave_function: function with three variables
        """      
        r1 = np.linalg.norm(r[:3,:], axis = 0)
        r2 = np.linalg.norm(r[3:,:], axis = 0)
        r12 = np.linalg.norm(r[:3,:]-r[3:,:], axis = 0)
        trial_wave = np.exp(-2*r1 - 2*r2 + r12/(2*(1+alpha*r12)))
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
         r: matrix of shape 6 x N x n_walkers
             N , number of steps
             n_walkers , number of walkers
             :3 x N x n_walkers , distance between proton and electron 1
             3: x N x n_walkers , distance between proton and electron 2

         Results
         -------
         E_loc: function with two variables
        """  
        r1_unit = r[:3,:,:] / np.linalg.norm(r[:3,:,:], axis = 0)
        
        r2_unit = r[3:,:,:] / np.linalg.norm(r[3:,:,:], axis = 0)
        r12_unit = r1_unit - r2_unit
        r12 = np.linalg.norm(r[:3,:,:] - r[3:,:,:], axis = 0)
        E_loc = -4 + np.sum(r12_unit * (r[:3,:,:] - r[3:,:,:]), axis = 0) * 1/(r12*(1+alpha*r12)**2) - 1/(r12*(1+alpha*r12)**3) - 1/(4*(1+alpha*r12)**4) + 1/r12
        #E_loc = np.reshape(E_loc, E_loc.shape[0]*E_loc.shape[1])
        return(E_loc)
    
    def der_ln_twf(self, alpha, r):
        """
         derivative of the natural logarithm of the trial wave function with respect to alpha, 
         needed to calculate the alpha derivative of the energy
         Parameters
         ----------
         r: matrix of shape 6 x N x n_walkers
            N , number of steps
            n_walkers , number of walkers
            :3 x N x n_walkers , distance between proton and electron 1
            3: x N x n_walkers , distance between proton and electron 2
    
         Results
         -------
         dln(trial_wavefunction)/dalpha: function with two variable
        """
        r12 = np.linalg.norm(r[:3,:]-r[3:,:], axis = 0)
        d_ln_twf = r12**2/(-2*(1+alpha*r12))
        return(d_ln_twf)
