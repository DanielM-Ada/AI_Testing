import random

def perceptron(inputs, weights, threshold):
    weighted_sum = sum(x * w for x, w in zip(inputs, weights))
    return 1 if weighted_sum >= threshold else 0

def train_perceptron(data, learning_rate=0.1, max_iter=1000):

    # max_iter is the maximum number of training cycles to attempt
    # until stopping, in case training never converges.

    # Find the number of inputs to the perceptron by looking at
    # the size of the first input tuple in the training data:
    first_pair = data[0]
    num_inputs = len(first_pair[0])

    # Initialize the vector of weights and the threshold:
    weights = [random.random() for _ in range(num_inputs)]
    threshold = random.random()
   
    # Try at most max_iter cycles of training:
    for _ in range(max_iter):

        # Track how many inputs were wrong this time:
        num_errors = 0
        
        # Loop over all the training examples:
        for inputs, desired_output in data:
            output = perceptron(inputs, weights, threshold)
            error = desired_output - output
            
            if error != 0:
                num_errors += 1
                for i in range(num_inputs):
                    weights[i] += learning_rate * error * inputs[i]
                threshold -= learning_rate * error
        
        if num_errors == 0:
            break
    
    return weights, threshold

and_data = [
 ((0, 0),  0),
 ((0, 1),  0),
 ((1, 0),  0), 
 ((1, 1),  1)
]

#and_weights, and_threshold = train_perceptron(and_data)

#print("Weights:", and_weights)
#print("Threshold:", and_threshold)

def and_function(x):
    weight = [0.574893577000916, 0.3106677061549179]
    threshold = 0.6994814205066435
    print(perceptron(x, weight, threshold))

first = (1,0)
and_function(first)
second = (1,1)
and_function(second)




