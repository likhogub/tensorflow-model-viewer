###Tensorflow 1.15
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model

###Specify filename of model
filename = 'your_model.h5'

###Converts float to RGB code 
def color(c):
    if abs(c) > 1:
        c = abs(c)/c
    r = 1
    g = 1
    b = 0
    if c > 0:
        r -=abs(c)
    else:
        g -=abs(c)
    return (r, g, b)

###Loading model weights
model = load_model(filename).get_weights() 

###Drawing inputs
for i in range(len(model[0])):
    plt.scatter(0, i, color="gray", zorder=5)

###Drawing neurons
for layer in range(1, len(model), 2):
    for neuron in range(len(model[layer])):
        plt.scatter(layer, neuron, color=color(model[layer][neuron]), zorder=5)

###Drawing connections between neurons
for layer in range(0, len(model), 2):
    for neuron in range(len(model[layer])):
        for next_neuron in range(len(model[layer][neuron])):
            if (layer==0):
                prev_layer = layer
            else:
                prev_layer = layer - 1
            plt.plot((prev_layer,layer+1), (neuron, next_neuron), color=color(model[layer][neuron][next_neuron]), linewidth = 1)

plt.show()