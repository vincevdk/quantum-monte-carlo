import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.helium_atom import Helium_atom

helium_atom = Helium_atom(6)
dim = helium_atom.dimension
alpha = minimization_alpha(helium_atom)

steps = np.linspace(0,len(alpha),len(alpha))

plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')
plt.show()