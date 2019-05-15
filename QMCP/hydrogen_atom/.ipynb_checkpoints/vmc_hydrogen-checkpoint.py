import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.hydrogen_atom import Hydrogen_atom

N = 30000 # number of steps
n_walkers = 400 # number of walkers

hydrogen = Hydrogen_atom(3)
alpha = np.arange(0.8, 1.3, 0.1)

E_ground, E_ground_error, variance, var_error = vmc(alpha, hydrogen, N, n_walkers)

plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
plt.xlabel(r'$\alpha$')
plt.ylabel('E')
plt.title('ground state energy')

plt.figure()
plt.errorbar(alpha, variance, yerr=var_error)
plt.title('variance')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\sigma^2$')
plt.show()



