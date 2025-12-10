x=[1.0,-2.0,3.0] #input values 
w=[-3.0,-1.0,2.0] #weights 
b=1.0 #bais 
xw0=x[0]*w[0]
print(xw0)
#and the output is:-3.0
xw0=x[0]*w[0]
xw1=x[1]*w[1]
xw2=x[2]*w[2]
print(xw1,xw2)
#and the output is:2.0,6.0 
print(xw0,xw1,xw2,b)
z=xw0+xw1+xw2+b 
print(z)
#and the output is:-3.0 2.0 6.0 1.0 6.0 
y=max(z,0)
print(y)
#and the output is:-3.0 2.0 6.0 1.0   6.0 6.0 Relu

