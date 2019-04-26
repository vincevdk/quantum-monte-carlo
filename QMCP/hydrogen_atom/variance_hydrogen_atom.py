import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt

#class quantum_system:
#    def __init__(self, trial_wave_function):
#        self.trial_wave_function = trial_wave_function
#        self.E_loc = E_loc
#        self.der_ln_twf = der_ln_twf

def trial_wave_function(alpha, R):
    return(np.exp(- alpha * R))

def E_loc(alpha, R):
    return(-1/R-alpha*(alpha-2/R)/2)

#hydrogen = quantum_system(lambda alpha,R:np.exp(- alpha * R), lambda alpha,R: -1/R-alpha*(alpha-2/R)/2, lambda R:-R)
alpha = np.arange(0.8, 1.2, 0.1)
dimension = 3

E_ground, variance = (vmc(alpha,trial_wave_function,E_loc, dimension))

print(E_ground,'E_ground')
plt.figure()
plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha

## variational quantum monte carlo simulation                                                
## initialize                                                                                

N = 10000


