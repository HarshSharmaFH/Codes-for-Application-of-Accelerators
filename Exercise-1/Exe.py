import random
import numpy as np
x=int(input("Enter the index of square matrix = "))
#y=int(input("Enter the number of columns = "))
m1=[]
for i in range(x):
    c1=[]
    for j in range(x):
        v1=random.randrange(-9999,9999)
        c1.append(v1)
    m1.append(c1)
print("A = ",m1)
m2=[]
for i in range(x):
    c2=[]
    for j in range(x):
        v2=random.randrange(-9999,9999)
        c2.append(v2)
    m2.append(c2)
print("B = ",m2)
matrix_multiply=np.dot(m1,m2)
print("A X B = ",matrix_multiply)
print()
#comment
