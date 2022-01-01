import random
import numpy as np
from numpy import interp
import math
def rateCodingDeterministicPix2Spike(pVal):
    T = 100 # ms
    freqHigh = 200 # Spike/sec
    freqLow = 10 # Spike/sec 
    '''
        1. Calculated the low and high frequencies using the retinal firing rates (10,200)
    '''
    ffs = freqHigh * T * 1/1000 # full frequency state
    lfs = freqLow * T * 1/1000  # low frequency state
    '''
        2. Interpolate the input pixel intensity value using the retinal firing rates as points
    '''
    f_det = interp(pVal, [0,lfs], [1,ffs]) # deterministic frequency
    '''
        3. Generate the spike emission interval
    '''
    spike_emission_interval = int(T/f_det) # spike emission interval
    '''
        4. Use the interval to fill out a spike train of size T (100 in our case)
    '''
    spike_train = np.asarray([1 if i % spike_emission_interval == 0 else 0 for i in range(1,T+1)]) # Generate a spike at each spike_emission_interval count
    return (spike_train)
print(rateCodingDeterministicPix2Spike(0.788))