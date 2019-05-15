import numpy as np
import matplotlib.pyplot as plt

def metropolis(function, N, n_walkers, dim):
    """
    Obtains a sequence of random samples from a probability distribution 
    from which direct sampling is difficult. 

    Parameters
    ----------
    function: function
    N:
    n_walkers:
    dim
       
    Results
    -------   
    rn:
    """

    rn = np.zeros((dim, N, n_walkers))
    r = np.random.randn(dim, n_walkers)
    
    for i in range(N):
        r_trial = r + (0.1*np.random.randn(dim, n_walkers))
        ratio = (function(r_trial) / function(r))**2
        eta = np.random.uniform(0,1,(dim,n_walkers))
        rn[:,i,:] = np.where(ratio >= 1, r_trial, (np.where(eta < ratio, r_trial, r)))
        r = np.where(ratio >= 1, r_trial, (np.where(eta < ratio, r_trial, r)))
    
    rn = np.reshape(rn[:,4000:,:], (dim,n_walkers*N - (n_walkers * 4000)))

    return(rn)


