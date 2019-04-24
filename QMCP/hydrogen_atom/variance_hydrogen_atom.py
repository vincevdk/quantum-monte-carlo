import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt

def trial_wave_function(alpha, R):
    return(np.exp(- alpha * R))

def E_loc(alpha, R):
    return(-1/R-alpha*(alpha-2/R)/2)


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
