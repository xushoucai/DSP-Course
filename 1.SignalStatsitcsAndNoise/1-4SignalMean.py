#Mean is represent my μ (sum/N)

#Standard Deviation
#|xi-μ| is how far i deviates from the mean
# Average deviation is sum/N
# This is not common in signals
# Standard Deviation: σ (sigma)
# square root of 1/(N-1) * sum( (xi-μ)^2 ) from i=0 to N-1
# Variance is σ^2
# Root Mean Square  = σ 

import numpy as np
import mysignals as sigs

signal_mean = np.mean(sigs.InputSignal_1kHz_15kHz)
print(signal_mean)






