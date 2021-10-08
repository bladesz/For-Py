'''
NNFS, https://nnfs.io

Neural Networks
Due 31/2/21
By; Roy Luo


'''
import numpy as np
import matplotlib


'''
Section 1 Part of a Neuron
'''
def activation(value):
    if value > 0:
        return True
    else:
        return False

weight = 0.4
inputs = 0.1
bias = 0.6
output = weight*inputs + bias
print(output)
print(activation(output))

'''
Section 2 A neuron in layer 1
'''

inputs = [1,2,3]
weights = [0.2, 0.8, -0.5]
bias = 2
#output = inputs[0]*weights[0]+\
#         inputs[1]*weights[1]+\
#         inputs[2]*weights[2]+\
#         bias

outputs = np.dot(weights, inputs) + bias
print(outputs)

'''Layer 1'''

inputs = [1,2,3,2.5]
weights = [[0.2, 0.8, -.5, 1],\
           [0.5, -.91, .26, -.5],\
           [-.26, -.27, .17, .87]]
biases = [2,3,.5]

#def layer_output(inputs, weights, biases):
#    layer_outputs = []
#    for neuron_weights, neuron_bias in zip(weights, biases): #zip is to assign i th value
#        neuron_output = 0
#        for n_input, weight in zip(inputs, neuron_weights):
#            neuron_output += n_input * weight
#        neuron_output += neuron_bias
#        layer_outputs.append(neuron_output)
#    return layer_outputs

layer_outputs = np.dot(weights, inputs) + bias
print(layer_outputs)



'''Tensor object is an that can represented by an array'''

'''
Section 3
'''

inputs = [[1.0,2.0,3.0,2.5],\
          [2.0,5.0,-1.0,2.0],\
          [-1.5,2.7,3.3,-0.8]]
weights = [[0.2, 0.8, -.5, 1],\
           [0.5, -.91, .26, -.5],\
           [-.26, -.27, .17, .87]]
biases = [2.0,3.0,.5]

weights2 = [[0.1, -0.14, 0.5],\
           [-0.5, 0.12, -0.33],\
           [-0.44, 0.73, -0.13]]
biases2 = [-1.0,2.0,-0.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
print(layer2_outputs)


'''Training Data with class based implementation of a simple forward pass that does not take with each neuron being independent from eachother'''

from nnfs.datasets import spiral_data
import nnfs
import matplotlib.pyplot as plt

nnfs.init() #sets default generation seed

class Layer_Dense:

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Rectified_Activation:

    def forward(self,inputs):
        self.output = np.maximum(0, inputs)


'''softmax activation function, used for classification '''

class Softmax_Activation:

    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True)) #negative max exists to prevent overflows
        probablities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probablities


x,y= spiral_data(samples=100, classes=3)

dense1 = Layer_Dense(2,3)
dense1.forward(x)

dense2 = Layer_Dense(3,3)

activation1 = Rectified_Activation()
activation1.forward(dense1.output)

dense2.forward(activation1.output)

activation2 = Softmax_Activation()
activation2.forward(dense2.output)
#print(activation2.output)

import math

class Loss: #calculates how confident the algorithmn is (parent)

    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CatergoricalCrossEntrophy(Loss): #inherits Loss

    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
        if len(y_true.shape)==1:
            correct_confidences = y_pred_clipped[\
                range(samples),\
                y_true
            ]

        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(\
                y_pred_clipped*y_true,\
                axis = 1
            )

        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

class Accuracy:
    
    def calculate(self, output, y):
        prediction = np.argmax(output, axis = 1)
        if len(y.shape)==2:
            y = np.argmax(y, axis=1)
        accuracy = np.mean(prediction == y)
        return accuracy




loss_function = Loss_CatergoricalCrossEntrophy()
loss = loss_function.calculate(activation2.output, y)

accuracy = Accuracy()
print(loss)
print(accuracy.calculate(activation2.output, y))

