#Write a python function with the name of "get_rigidity" to calculate the magnetic rigidity 
import numpy as np
global e,c
e=1.60e-19;  # in C
c=3e8       # in m/s
u=1.66054e-27 # u in kg
class particle:
    def __init__(data,a,q,T):    
        data.a=a
        data.q=q
        data.T=T*data.a*e*1e6  #kinetic energy in MeV
    def get_rigidity(data):
        E_0= data.a*u*c**2     #rest mass energy in J
        E=E_0+data.T           #total energy in J
        Bp=np.sqrt(E**2-E_0**2)/(c*data.q*e)  #calculation of rigidity
        print("\nRest mass energy (E_0)= " "{:.3E}".format(E_0), 'J')
        print("\nTotal energy (E)= " "{:.3E}".format(E), 'J')
        print("\nThe magnetic rigidity for is= " "{:.3E}".format(Bp), 'Tm')
    def __str__(data):
        return f"Atomic Mass = {data.a}\nCharge = {data.q}\nKinetic Energy in J = {data.T}"     
x_1=particle(238,28,190) # input atomic mass, charge and kinetic energy in AMeV
x_2=particle(197,77,410)
x_3=particle(0.000549,1,1.8215e7)
print("Q1)\n", x_1)
x_1.get_rigidity()
print("\n---------------------------")
print("Q2)\n", x_2)
x_2.get_rigidity()
print("\n---------------------------")
print("Q3)\n", x_3)
x_3.get_rigidity()
print("\n---------------------------")
"""
Created on Thu Jan 5 ,2023

@author: Harsh
"""