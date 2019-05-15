import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.helium_atom import Helium_atom

N = 30000 # number of steps
n_walkers = 400 # number of walkers

helium_atom = Helium_atom(6)
alpha = minimization_alpha(helium_atom, N, n_walkers)

steps = np.linspace(0,len(alpha),len(alpha))

plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')
plt.xlabel('steps')
plt.ylabel(r'$\alpha$')
plt.show()