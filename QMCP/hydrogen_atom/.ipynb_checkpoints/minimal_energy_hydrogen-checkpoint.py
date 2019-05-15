import time
import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.hydrogen_atom import Hydrogen_atom

N = 30000 # number of steps
n_walkers = 400 # number of walkers

hydrogen = Hydrogen_atom(3)
alpha = minimization_alpha(hydrogen, N, n_walkers)

steps = np.linspace(0,len(alpha),len(alpha))

print(steps,'steps')
plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')
plt.xlabel('steps')
plt.ylabel(r'$\alpha$')
plt.show()
