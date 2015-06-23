def step_function(x):
    return 1 if x >= 0 else 0

# Because it is discontinouous, we can't use the above
# function to train a neural network

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

# We can use combinations of perceptrons to create
# various logic gates

def perceptron_output(weights, bias, x):
    calculation = dot(weights, x) + bias
    return step_function(calculation)

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))
