import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt
from QMCP.functions import bootstrap
from QMCP.helium_atom import Helium_atom

alpha = np.linspace(0.05, 0.25, 6)
helium_atom = Helium_atom(6)
dim = helium_atom.dimension
E_ground, E_ground_error, variance = vmc(alpha, helium_atom)

print(E_ground)
plt.figure()
#plt.errorbar(alpha, E_ground, yerr=E_ground_error)
plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()
