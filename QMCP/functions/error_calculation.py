import numpy as np

def select_random_set(data_points, n_iterations, blocksize):
    """ Chooses a random set from  N data points of size : "set_size" where 
    a single point can be chosen several times. Does this "n_iterations" 
    times.
        
    Parameters:
    -----------
    date_points: array of size Nt
       Note that the function works for any array size.
    n_iterations: int
       Number of times a random set should be chosen

    Results:
    --------
    random_data_points: array of size (n_iteaterations, set_size)
    """
    random_data_points = np.random.choice(data_points, 
                                          size = (n_iterations, 
                                                  blocksize))
    return(random_data_points)

def bootstrap(N_data_points, n_iterations):
    """ Calculates the error using the bootstrap method. From N data points 
    a new random set is chosen by drawing "set_size" random data points from 
    the  original set, where a single point can be chosen several times. From 
    this new data set the time average is calculated, call this A. This 
    process of choosing a random set and calculating the average is repeated  
    n_iteration times. From these n values a standard deviation is calculated.

    Parameters:                                                               
    -----------                                       
    N_data_points: array of size Nt
        can be any size
    n_iterations: int
        number of times a random data set is chosen and the average is 
        computed. For the bootstrapping to work correctly, n_iterations 
        should be large enough such that the calculated error does not 
        change when further increasing n_iterations. 

    Results:                                      
    --------  
    energy_standard_deviation: float
       calculated using the following formula σA​= (⟨A**2⟩−⟨A⟩**2)**0.5
    var_average:
    var_standard_deviation:
    
    """
    blocksize = 10000

    random_set = select_random_set(N_data_points, n_iterations, blocksize)

    var_vec = np.var(random_set,axis=1)
    var_average = np.mean(var_vec)
    var_standard_deviation = np.std(var_vec)
#    var_standard_deviation = calculate_standard_deviation(var_vec, n_iterations)
    average_random_set = np.mean(random_set, axis = 1)
    energy_standard_deviation = np.std(average_random_set)
    energy_standard_deviation = np.std(average_random_set)
    return(energy_standard_deviation, var_average, var_standard_deviation)

