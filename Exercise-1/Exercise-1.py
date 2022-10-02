#Write a function in Python code that multiples 2 (two) 3x3 Matrices (ndarray) and returns the result.
#Call this function using two randomly generated 3 by 3 matrices and print the results.
import random
import time
import numpy as np
x=int(input("Enter the order of square matrix = "))
def getMatrix(x):
    m=[]
    for i in range(x):
        c=[]
        for j in range(x):
            v=random.randrange(-99,99)
            c.append(v)
        m.append(c)
    return m
A=getMatrix(x)
B=getMatrix(x)
print("A = ",A," \n","B = ",B)
C=np.dot(A,B)
print("A X B = ","\n",C)
time.sleep(30)
