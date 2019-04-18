import numpy as np
import matplotlib.pyplot as plt

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
    return(x)



