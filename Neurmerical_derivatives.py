import numpy as np
def f(x):
    return 2*x**2 
#np.arange(start,stop,step)to give us smoother line 
x=np.arange(0,5,0.0001)
y=f(x)
p2_delta=0.0001 
x1=2
#the point and the "close enough"point
x2=x1+p2_delta
y1=f(x1)
y2=f(x2)
print((x1,y1),(x2,y2))
#derivative approximation and y-itercept for the tangent line
approximate_derivative=(y2-y1)/(x2-x1)
b=y2-approximate_derivative*2 
'''
we put the tangent line calculating into a function so we call 
it multiple times for different values of x 
approximate_derivative and b are contant for given function
thus calculated once above this function
'''
def tangent_line(x):
    return approximate_derivative*x+b 
'''
import matplotlib.pyplot as plt
to_plt=[x1-0.9,x1,x1+0.9]
plt.plot'''
print('approximate_derivative for f(x)',
      f'where x={x1} is {approximate_derivative}')
#and the output is:(2,8)(2.0001,8.000800020000002)
#approximate_derivative for f(x) where x=2 is 8.000199999998785
'''
import maplotlib.pyplot as plt 
import numpy as np 
def f(x):
    return 2*x**2 
#np.arange(start,stop,step) to give us a smoother curve 
x=np.array(np.arange(0.5,0.0001))
y=f(x)
plt.plot(x,y)
colors=['k','g','r','b','c']
def approximate_tangent_line(x,approximate_derivative):
    return (approximate_derivative*x)+b
for i in range(5):
    p2_delta=0.0001 
    x1=i 
    x2=x1+p2_delta 
    y1=f(x1)
    y2=f(x2)
    print((x1,y1),(x2,y2))
    approximate_derivative=(y2-y1)/(x2-x1)
    b=y2-(approximate_derivative*2)
    to_plot=[x1-0.9,x1,x1+0.9]
    plt.scatter(x1,y1,c=colors[i])
    plt.plot([point for point in to_plot],
             [approximate_tangent_line(point,approximate_derivative)
               for point in to_plot],
             c=colors[i])
    print('approximate derivative for f(x)'
          f'where x={x1} is {approximate_derivative}')
plt.show()

'''

