import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.functions import bootstrap
from QMCP.helium_atom import Helium_atom

N = 30000
n_walkers = 400

alpha = np.linspace(0.05, 0.25, 8)
helium_atom = Helium_atom(6)

E_ground, E_ground_error, variance, var_error = vmc(alpha, helium_atom, N, n_walkers)

print(E_ground_error, 'E_ground_error')
print(E_ground, 'E_ground')
print(variance, 'variance')
print(var_error,'variance error')
plt.figure()
plt.errorbar(alpha, E_ground, yerr=E_ground_error)
#plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.errorbar(alpha, variance, yerr=var_error)
#plt.plot(alpha, variance)
plt.title('variance')
plt.show()
