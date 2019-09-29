#%%Importing libraries
import numpy as np
import random
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d

#%%Rosenbrock Function
def rosenbrock(x,y,a=1,b=100):
    return ((a-x)**2 + b*(y-x**2)**2)

x=np.random.uniform(-5, 5)
y=np.random.uniform(-5, 5)

#%%Simple Monte Carlo
t=[]

X=[]
Y=[]
s=rosenbrock(x,y)
t.append(s)
X.append(x)
Y.append(y)

for i in range(0,2000):
    h1=random.uniform(-1, 1)
    h2=np.random.uniform(-1,1)
    x1=x+h1
    y1=y+h2
        
    fx1=rosenbrock(x1,y1)
    if ((s-fx1)>=0):
        x=x1
        y=y1
        s=fx1
        
        
        X.append(x)
        Y.append(y)
        t.append(s)
        print("x is %f and y is %f and energy is %f"%(x1,y1,fx1))
#aa=plt.figure()     #For plotting uncomment onwards
#ax=plt.axes(projection='3d')
#ax.plot3D(X,Y,t,'red')
#plt.show()        
        
   

