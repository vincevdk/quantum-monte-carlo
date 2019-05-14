import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.hydrogen_atom import Hydrogen_atom

N = 30000
n_walkers = 400

hydrogen = Hydrogen_atom(3)
alpha = np.arange(0.8, 1.2, 0.1)

E_ground, E_ground_error, variance, var_error = vmc(alpha, hydrogen, N, n_walkers)

print(E_ground,'E_ground')
plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
#plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.errorbar(alpha, variance, yerr=var_error)
#plt.plot(alpha, variance)
plt.title('variance')
plt.show()



