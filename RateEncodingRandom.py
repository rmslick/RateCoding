import random
import numpy as np
import math
# Takes in pixel and returns spike train
def rateCodingRandPix2Spike(pVal,tu):
    spikeTrain = [1 if pVal > random.random() else 0 for i in range(tu)]
    return np.asarray(spikeTrain)
# Normalizes 2d image between 0 and 1
def norm2D(image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))
def rateCodingRand2D(image):
    # 1. Normalize the input image
    image = norm2D(image)
    # 2. Set a firing rate, T
    T = 100  # Set to spike train interval 100ms
    # 3. Using T obtain time axis 
    dt = 1  # (T = 100ms -> dt = 1000ms/100 = 1ms)
    bins = int(T / dt)  # time axis length of 100 units
    random.seed(9)
    # 4. For each normalized pixel value in , pVal, in image and for each 
    # time unit T, generate a random number, r from range (0,1). 
    # If pVal > r then store a spike at that time instant otherwise 0.
    for x in image:
        for y in x:
            spikeTrain = rateCodingRandPix2Spike(y,bins)
            print('Normal val',y,'fired on',(len([i for i in spikeTrain if i == 1]))/bins,'%')