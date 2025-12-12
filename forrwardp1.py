#forward pass 
x=[1.0,-2.0,3.0] #inputs
w=[-3.0,-1.0,2.0] #weights
b=1.0  #bias
#mutiplying inputs by weights
xw0=x[0]*w[0]
xw1=x[1]*w[1]
xw2=x[2]*w[2]
#adding weighted inputs and bias
z=xw0+xw1+xw2+b
#relu activation function
y=max(z,0)
#backward pass 
#the derivative from the next layer
dvalue=1.0
#derivative of relu and the chain rule
drelu_dz=dvalue*(1.if z > 0 else 0.)
print(drelu_dz)
#partial derivative of the multiplication,the cain rule
dsum_dxw0=1
drelu_dz=dvalue*(1. if z > 0 else 0.)
print(drelu_dz)
dsum_dxw0=1
drelu_dxw0=drelu_dz*dsum_dxw0
print(drelu_dxw0)
#and the output is:1.0 1.0
