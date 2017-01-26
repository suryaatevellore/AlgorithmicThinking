from __future__ import division
import matplotlib.pyplot as plt

##Refer to the equation here 

big = {}
for i in xrange(1000):
  big[i]=3*i+5

##function2
func2={}
for i in xrange(1000):
    func2[i]=8*i
plt.plot(big.keys(),big.values(),'r')
plt.plot(func2.keys(),func2.values(),'b')
plt.show()

