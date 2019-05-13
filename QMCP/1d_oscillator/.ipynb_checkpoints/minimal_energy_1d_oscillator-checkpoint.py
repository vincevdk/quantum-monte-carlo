import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import metropolis
from QMCP.functions import minimization_alpha

## variational quantum monte carlo simulation
## initialize

N = 10000

def trial_wave_function(R, alpha):
    return(np.exp(- alpha * R**2))

def E_loc(alpha, R):
    return(alpha + (R**2)*(0.5 - 2*alpha**2))

alpha = minimization_alpha(trial_wave_function, E_loc)
_ = np.linspace(0,len(alpha),len(alpha))
plt.title('minimization of alpha')
plt.plot(_,alpha, 'ro')

plt.show()
