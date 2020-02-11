import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,2)
print(x)
print("------")
f=open("linsp.txt","w")
y=-x*np.sin(2*x)*2
print (y)
f.write(str(x))

plt.plot(x,y)
plt.show()

