import numpy as np
import matplotlib.pyplot as plt


def trial_wave_function(R):
    return(np.exp(- 0.5 * R**2))

def metropolis(function, N):
    x = np.zeros(N)
    x[0] = 0.1
    h = 1/10
    t = 0

    for i in range(len(x)):
        x_trial = np.random.uniform(-h/2, h/2)
        x_trial = x[i-1] + x_trial

        r = (function(x_trial)/function(x[i-1]))**2
        if r >= 1:
            t = t + 1
            x[i] = x_trial

        else:
            eta = np.random.uniform(0,1)
            if eta < r:
                x[i] = x_trial
            else:
                x[i] = x[i-1]
    acceptance_ratio = t/len(x)
    print(acceptance_ratio, 'acceptance ratio')

    return(x)

if __name__=='__main__':
    density = metropolis_algorithm(trial_wave_function,100000)
    plt.figure()
    count, bins, ignored = plt.hist(density[1000:], 30, density=True)
    plt.plot(bins, 1/(0.5 * np.sqrt(2 * np.pi)) * np.exp( - (bins)**2 / (2 * 0.5**2) ),linewidth=2, color='r')
    plt.show()
#plt.figure()
#plt.plot(alpha, E_ground)
#plt.title('ground state energy')

