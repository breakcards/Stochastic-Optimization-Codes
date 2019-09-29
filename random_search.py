#%%importing libraries
import numpy as np
import random
#import matplotlib.pyplot as plt
import pandas as pd

#%%Rosenbrock Function
def rosenbrock(x,y,a=1,b=100):
    return ((a-x)**2 + b*(y-x**2)**2)

x=np.random.uniform(-5, 5)
y=np.random.uniform(-5, 5)

#%%Random Search
t=[]
q=[]
l=[]
w=[]
s=rosenbrock(x,y)
for i in range(0,500):
    h=random.uniform(-1, 1)
    q=rosenbrock(x+h,y+h)
    l.append(x+h)
    w.append(y+h)
    t.append(q)
z=np.array([[l],[w],[t]])
aa=pd.DataFrame(np.transpose(z.reshape(3,500)),columns=["x","y","fx"])  #resulting data frame
