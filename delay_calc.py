import matplotlib.pyplot as plt
import numpy as np

fs         = 8000.0
f         = 475 # starting frequency
fdev        = 11 #deviation freq
fstep         = 50
delay_stop     = 250 # stop time

def max_calc(f):

    Diff = 0
    Amax = 0
    Delmax = 0
    res = []
    x = []
    for i in range(1, delay_stop):
        delay = i * (1/fs)
        Diff = np.cos(2 * np.pi * (f - fdev) * delay)-np.cos(2 * np.pi * (f + fdev)* delay)
        res.append(Diff)
        if (Diff > Amax):
            Amax = Diff
            Delmax = delay
    return Amax, Delmax, Delmax/(1/fs)

#Amax, Delmax,x = max_calc(f)
#print (Delmax,x)

for i in range (0,10):

    Amax, Delmax, x = max_calc(f+i*fstep)
    ("--------------------------------------------")
    print (str (f + i * fstep) + " Hz")
    print (Amax)
    print 
    print (Delmax, x)
    print ("--------------------------------------------")
    print()

#plt.plot(x, res, 'b')
#plt.plot(x, res, 'b')
#plt.show()

