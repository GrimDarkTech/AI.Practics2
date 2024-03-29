from neuronpy import Neuron
from neuronpy import Activations

import layerpy

import networkpy

inputValues = []

weightsL = [1, -0.1, -1,
            1, -0.1, -1,
            1, -0.1, -1,
]
weightsM = [-0.1, 1, -0.1,
            -0.1, 1, -0.1,
            -0.1, 1, -0.1,
]
weightsR = [-1, -0.1, 1,
            -1, -0.1, 1,
            -1, -0.1, 1,
]

inputArray = []
print("Enter input values (3x3 array)")
for i in range(0,3):
    inputArray.append(input().split(","))
for arr in inputArray:
    for val in arr:
        inputValues.append(float(val))

neurons = []

neuron = Neuron(inputValues, weightsL, Activations.sigmoid, False)
neurons.append(neuron)

layer = layerpy.Layer(neurons)

layer.calculate()

print(layer.outputs)

print("Press any key to exit")
input()
