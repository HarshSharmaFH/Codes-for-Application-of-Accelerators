#Write a function in Python code that multiples 2 (two) 3x3 Matrices (ndarray) and returns the result.
#Call this function using two randomly generated 3 by 3 matrices and print the results.
"""
import random
n=int(input("Number = "))
x=[]
for i in range(n):
    v=input(random.randint(-99,99))
    x.append(v)
print(x)


import random
x=int(input("Enter the number of rows = "))
y=int(input("Enter the number of columns = "))
m_1=[]
for i in range(x):
    c=[]
    for j in range(y):
        v=input(random.randint(-99,99))
        c.append(v)
    m_1.append(c)
print(m_1)
for i in range(x):
    for j in range(y):
        print(m_1[i][j],end="")
    print()      
"""
import random
import numpy as np
def getmatrix(num1,num2):
  m1 = [[0 for _ in range(num2)] for _ in range(num1)]
  for i in range(num1):
    for j in range(num2):
      v=random.randint(-99,99)
      m1[i][j]=v
      print(m1)
x=int(input("Enter the number of rows = "))
y=int(input("Enter the number of columns = "))
matrix_1=getmatrix(x,y)
matrix_2=getmatrix(x,y)
multiply=np.dot(matrix_1,matrix_2)
print(multiply)


