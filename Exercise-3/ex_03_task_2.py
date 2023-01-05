#From the accelerator department, you received some data  from an ionisation beam profile monitor(IPM). 
#Read the file and plot it in blue color on a black grid background. The mark the maximum with a red dot! 
#Code and plot (PNG) as usual on GitHUB.
from numpy import argmax,max
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel(r'C:/Users/Harsh Sharma/Desktop/data.xlsx',sheet_name='data')    
x_0 = list(data['x'])
y_0 = list(data['y'])
x_max=x_0[argmax(y_0)]
y_max=max(y_0)
plt.plot(x_0,y_0,x_max,y_max,'rx')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.annotate(text='max value', xy=(x_max,y_max), xycoords='data',xytext=(800,27.5),
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.15"))
plt.grid(True)
plt.savefig('figure', dpi=240)
plt.show()
"""
Created on Thu Jan 5 ,2023

@author: Harsh Sharma
"""