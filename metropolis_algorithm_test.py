import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from metropolis_algorithm import metropolis


def example_1d_oscillator():
    f= lambda x:np.exp(-0.5*x**2)
    p_r = lambda r:(np.exp(-2*0.5*r**2))/(np.sqrt(np.pi))

    density = metropolis(f,400000)
    plt.figure()
    plt.title(r'$\rho(x) = \frac{e^{-2\alpha x^2}}{\int e^{-2\alpha x^2} dx}$') 
    count, bins, ignored = plt.hist(density[1000:], 100, density=True)
    plt.plot(bins, p_r(bins),linewidth=2, color='r')
    plt.show()

def example_helium():
    g = lambda x:np.exp(-2)*np.exp(-4)*np.exp(2/(2*(1+x*2)))
    int = integrate.quad(g, -1000, 1000)
    p_r = lambda r:np.exp(-2*0.5*r**2)/int[0]

    density = metropolis(g,100000)
    plt.figure()
    plt.title('helium')
    count, bins, ignored = plt.hist(density[1000:], 30, density=True)
    plt.plot(bins, p_r(bins),linewidth=2, color='r')

if __name__ == '__main__':
    example_1d_oscillator()
#    example_helium()
    plt.show()

