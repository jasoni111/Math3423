import numpy as np

def ggwp(a,b):
    X = np.random.normal(15,4,100)
    x= np.mean(X)
    t = x*(x+3)
    return a<t<b

print(ggwp(244.128,296.4874) )

acc = 0
for _ in range(1000000):
    acc += ggwp(244.128,295.872)
print(acc / 1000000.0 )