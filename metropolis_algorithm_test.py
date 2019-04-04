import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from metropolis_algorithm import metropolis


def example_1():
    def trial_wave_function(R):
        return(np.exp(- 0.5 * R**2))

    f= lambda x:np.exp(-2*0.5*x**2)
    int = integrate.quad(f, -1000, 1000)
    p_r = lambda r:np.exp(-2*0.5*r**2)/int[0]

    density = metropolis(trial_wave_function,100000)
    plt.figure()
    plt.title(r'$\rho(x) = \frac{e^{-0.5\alpha x^2}}{\int e^{-\alpha x^2} dx}$') 
    count, bins, ignored = plt.hist(density[1000:], 30, density=True)
    plt.plot(bins, p_r(bins),linewidth=2, color='r')

if __name__ == '__main__':
    example_1()
    plt.show()
