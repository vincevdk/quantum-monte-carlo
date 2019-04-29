import numpy as np
from QMCP.functions import vmc
import matplotlib.pyplot as plt

class Hydrogen_atom:
     def __init__(self, dimension):
        self.dimension = dimension

     def trial_wave_function(self,alpha, R):
         return(np.exp(- alpha * R))

     def E_loc(self, alpha, R):
         return(-1/R-alpha*(alpha-2/R)/2)

     def der_ln_twf(self, R):
          return(-R)

hydrogen = Hydrogen_atom(3)
alpha = np.arange(0.8, 1.2, 0.1)

E_ground, variance = (vmc(alpha, hydrogen))

print(E_ground,'E_ground')
plt.figure()
plt.plot(alpha, E_ground)
plt.title('ground state energy')

plt.figure()
plt.plot(alpha, variance)
plt.title('variance')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha

## variational quantum monte carlo simulation                                                
## initialize                                                                                

N = 10000


