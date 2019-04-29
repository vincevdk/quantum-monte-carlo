import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.hydrogen_atom import Hydrogen_atom

alpha = minimization_alpha(Hydrogen_atom(3))
steps = np.linspace(0,len(alpha),len(alpha))
print(steps,'steps')
plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')

plt.show()
