import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.harmonic_oscillator import Oscillator
from QMCP.functions import bootstrap

N = 30000
n_walkers = 400

alpha = np.arange(0.1, 0.3, 0.05)
oscillator = Oscillator(1)
E_ground, E_ground_error, variance, var_error = vmc(alpha, oscillator, N, n_walkers)

print(E_ground_error, 'error E')
print(E_ground)
plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
#plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.errorbar(alpha, variance, yerr=var_error)
#plt.plot(alpha, variance)
plt.title('variance')
plt.show()
