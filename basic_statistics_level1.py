#Q6
#Expected value
import numpy as np
candiescount = np.array([1,4,3,5,6,2])
prob= np.array([0.015,0.2,0.65,0.005,0.01,0.120])

def expected_value(candiescount, prob):
    return (candiescount * prob).sum()/prob.sum()
expected_value(candiescount, prob)

#==========================================
