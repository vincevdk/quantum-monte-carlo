import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt

def trial_wave_function(alpha, R):
    return(np.exp(- alpha * R))

def E_loc(alpha, R):
    return(-1/R-1/2*alpha*(alpha-2/R))

alpha = np.arange(0.8, 1.2, 0.1)
range = 1
E_ground, variance = (vmc(alpha,trial_wave_function,E_loc, range))

print(E_ground,'E_ground')
plt.figure()
plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()
