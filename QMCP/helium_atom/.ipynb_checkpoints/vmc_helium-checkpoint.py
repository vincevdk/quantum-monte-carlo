import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.functions import bootstrap
from QMCP.helium_atom import Helium_atom

N = 30000 # number of steps
n_walkers = 400 # number of walkers

alpha = np.arange(0.05, 0.25, 0.025)
helium_atom = Helium_atom(6)

E_ground, E_ground_error, variance, var_error = vmc(alpha, helium_atom, N, n_walkers)

plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
plt.xlabel(r'$\alpha$')
plt.ylabel('E')
plt.title('ground state energy')

plt.figure()
plt.errorbar(alpha, variance, yerr=var_error)
plt.title('variance')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\sigma$^2')
plt.show()
