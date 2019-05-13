import numpy as np
import matplotlib.pyplot as plt
from QMCP.functions import minimization_alpha
from QMCP.harmonic_oscillator import Oscillator

oscillator = Oscillator(1)
alpha = minimization_alpha(oscillator)

steps = np.linspace(0,len(alpha),len(alpha))

plt.title('minimization of alpha')
plt.plot(steps,alpha, 'ro')
plt.show()
