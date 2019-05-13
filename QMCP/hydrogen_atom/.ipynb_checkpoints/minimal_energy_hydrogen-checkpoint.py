import time
import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.hydrogen_atom import Hydrogen_atom

start = time.time()
hydrogen = Hydrogen_atom(3)
dim = hydrogen.dimension
alpha = minimization_alpha(hydrogen)
steps = np.linspace(0,len(alpha),len(alpha))
print("If I'm not running parallel it takes" + str(time.time() - start))

print(steps,'steps')
plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')

plt.show()
