import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.harmonic_oscillator import Oscillator
from QMCP.functions import bootstrap

alpha = np.arange(0.1, 2, 0.05)
oscillator = Oscillator(1)
E_ground, E_ground_error, variance = (vmc(alpha, oscillator))

print(E_ground)
plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
#plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()
