import numpy as np 
import nnfs 
from nnfs.datasets import spiral_data
nnfs.init()
class Layer_dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights=0.01*np.random.randn(n_inputs,n_neurons)
        self.biases=np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output=np.dot(inputs,self.weights)+self.biases
class Activation_relu:
    def forward(self,inputs):
        self.output=np.maximum(0,inputs)
class Activation_softmax:
    def forward(self,inputs):
        exp_values=np.exp(inputs-np.max(inputs,axis=1,
                                        keepdims=True))
        probabilities=exp_values/np.sum(exp_values,axis=1,
                                        keepdims=True)
        self.output=probabilities
class Loss:
    def calculate(self,output,y):
        sample_losses=self.forward(output,y)
        data_loss=np.mean(sample_losses)
        return data_loss
class Loss_CategoricalCrossentropy(Loss):
    def forward(self,y_pred,y_true):
        samples=len(y_pred)
        y_pred_clipped=np.clip(y_pred,1e-7,1-1e-7)
        if len(y_true.shape)==1:
            correct_confidences=y_pred_clipped[
                range(samples),
                y_true
            ]
        elif len(y_true.shape)==2:
            correct_confidences=np.sum(
                y_pred_clipped*y_true,
                axis=1 
            )
        negative_log_likelihoods=-np.log(correct_confidences)
        return negative_log_likelihoods
x,y=spiral_data(samples=100,classes=3)
dense1=Layer_dense(2,3)
activation1=Activation_relu()
dense2=Layer_dense(3,3)
activation2=Activation_softmax()
loss_function=Loss_CategoricalCrossentropy()
dense1.forward(x)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)
print(activation2.output[:5])
loss=loss_function.calculate(activation2.output,y)
print('loss:',loss)
softmax_output=np.array([[0.7,0.2,0.1],
                         [0.5,0.1,0.4],
                         [0.02,0.9,0.08]])
class_target=np.array([0,1,1])
predictions=np.argmax(softmax_output,axis=1)
if len(class_target.shape)==2:
    class_target=np.argmax(class_target,axis=1)
accuracy=np.mean(predictions==class_target)
print('acc:', accuracy)
predictions=np.argmax(activation2.output,axis=1)
if len(y.shape)==2:
    y=np.argmax(y,axis=1)
accuracy=np.mean(predictions==y)
print('acc:',accuracy)
'''import matplotlib.pyplot as plt
from nnfs.datasets import vertical_data
nnfs.init()
x,y=vertical_data(samples=100,classes=3)
plt.scatter(x[:,0],x[:,1],c=y,s=40,cmap='brg')
plt.show()'''
from nnfs.datasets import vertical_data
nnfs.init()
x,y=vertical_data(samples=100,classes=3)
dense1=Layer_dense(2,3)
activation1=Activation_relu()
dense2=Layer_dense(3,3)
activation2=Activation_softmax()
loss_function=Loss_CategoricalCrossentropy()
lowest_loss=9999999
best_dense1_weights=dense1.weights.copy()
best_dense1_biases=dense1.biases.copy()
best_dense2_weights=dense2.weights.copy()
best_dense2_biases=dense2.biases.copy()
for iteration in range(10000):  
    dense1.weights+=0.05*np.random.randn(2,3)
    dense1.biases+=0.05*np.random.randn(1,3)
    dense2.weights+=0.05*np.random.randn(3,3)
    dense2.biases+=0.05*np.random.randn(1,3)
    dense1.forward(x)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    activation2.forward(dense2.output)
    loss=loss_function.calculate(activation2.output,y)
    if loss<lowest_loss:
        print('new lowest loss:',loss)
        lowest_loss=loss
        best_dense1_weights=dense1.weights.copy()
        best_dense1_biases=dense1.biases.copy()
        best_dense2_weights=dense2.weights.copy()
        best_dense2_biases=dense2.biases.copy()
    else:
        dense1.weights=best_dense1_weights.copy()
        dense1.biases=best_dense1_biases.copy()
        dense2.weights=best_dense2_weights.copy()
        dense2.biases=best_dense2_biases.copy()    
