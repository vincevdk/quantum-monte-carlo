import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt

def trial_wave_function(R, alpha):
    return(np.exp(- alpha * R**2))

def E_loc(alpha, R):
    return(alpha + (R**2)*(0.5 - 2*alpha**2))

alpha = np.arange(0.1, 2, 0.05)
E_ground, variance = (vmc(alpha,trial_wave_function,E_loc))

print(E_ground)
plt.figure()
plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()
