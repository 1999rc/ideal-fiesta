x=[1.0,-2.0,3.0] #input values 
w=[-3.0,-1.0,2.0] #weights 
b=1.0 #bias 
xw0=x[0]*w[0]
xw1=x[1]*w[1]
xw2=x[2]*w[2]
#adding weights inputs and bias 
z=xw0+xw1+xw2+b 
#Relu activation function 
y=max(z,0)
#backward pass 
dvalue=1.0 
#derivative of reul and the chain rule 
drelu_dz=dvalue*(1.if z > 0 else 0.)
print(drelu_dz)
#and the output is:1.0 
dsum_dxw0=1 
drelu_dxw0=drelu_dz*dsum_dxw0
print(drelu_dxw0)
#and the output is:1.0 1.0 
