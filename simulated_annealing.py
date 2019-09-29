# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:12:06 2019

@author: Nikhil Shinde
"""
#%%importing library
import numpy as np
#%%Rosenbrock Function
def rosenbrock(x,y):
    return (1-x)**2 + 100*((y-x**2))**2

#%%SA
x= np.random.uniform(-5,5)
y= np.random.uniform(-5,5)
E1 = rosenbrock(x,y)

Acp_energy=[];  Rej_energy=[]; X=[]; Y=[]
T = 1000
#%%To select initial temp T0
for i in np.arange(500):
    h1= np.random.uniform(-1,1)
    h2= np.random.uniform(-1,1)
    newX= x+h1
    newY= y+h2
    X.append(newX)
    Y.append(newY)
    E2 = rosenbrock(newX,newY)
    delta =E2-E1
    if delta <= 0 or np.random.uniform(0,1) < np.exp(-delta/T):
        x=newX
        y=newY
        E1=E2
        Acp_energy.append(E2) #Acccepted energy
    else :
        x=x
        y=y
        Rej_energy.append(E1) #Rejected energy

m1=len(Acp_energy)
m2= len(Rej_energy) 
f = np.mean(Rej_energy)
To = -f /(np.log((0.95* (m1+m2) -m1)/m2))
#print("Initial temp:",To)
T=To

#%%
x= np.random.uniform(-5,5)
y= np.random.uniform(-5,5)
E1 = rosenbrock(x,y)
energy =[]; X=[]; Y=[]

for i in np.arange(T):
    iter =1000
    for i in np.arange(iter):
        h1= np.random.uniform(-1,1)
        h2= np.random.uniform(-1,1)
        newX= x+h1
        newY= y+h2
        X.append(newX)
        Y.append(newY)
        E2 = rosenbrock(newX,newY)
        delta =E2-E1
        if delta <= 0 or np.random.uniform() < np.exp(-delta/T):
            x=newX
            y=newY
            E1=E2
            energy.append(E2)
        else :
            energy.append(E2)
    
    if len(energy) >= 100 or iter >= 100:
        T = T*0.9
        if T<=1:
            break

Min = np.argmin(energy)
x=X[Min];y = Y[Min]

print("The optimum value of rosenbrock function is:",rosenbrock(x,y))

print("\nThe optimum values of x & y are:",x,y)

print("\nInitial temp And Final Temp :",To ,T)
    
    

    
    
