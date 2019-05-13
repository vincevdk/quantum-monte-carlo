import time
import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import parallel_minimization_alpha
from QMCP.helium_atom import Helium_atum

start = time.time()

alpha = parallel_minimization_alpha(Helium_atom(6))
steps = np.linspace(0,len(alpha)-1,len(alpha))
print("My work is finished, I took " + str(time.time() - start))

print(steps,'steps')
plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')

plt.show()
