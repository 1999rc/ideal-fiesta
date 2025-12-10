import numpy as np 
def f(x):
    return x*2 
x=np.array(range(5))
y=f(x)
print(x)
#and the output is:[0,1,2,3,4]
                   #[0,2,4,6,8]
print((y[1]-y[0])/(x[1]-x[0]))
#and the output is:2.0 
def f(x):
    return x**x*2
y=f(x)
print(x)
print(y)
#and the output is:[0,1,2,3,4]
                  #[0,2,8,18,32]
print((y[1]-y[0])/(x[1]-x[0]))
#and the output is:2
print((y[3]-y[2])/(x[3]-x[2]))
#and the output is:10 
p2_delta=0.0001
x1=1
x2=x1+p2_delta 
y1=f(x1)
y2=f(x2)
approximate_derivative=(y2-y1)/(x2-x1)
print(approximate_derivative)
#and the output is:4.0001999999987845

