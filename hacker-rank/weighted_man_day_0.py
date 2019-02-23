# Capture all the inputs
length = input()
weights = input()
number = input()

# Transform all the values into int
length = int(length)
weights = map(int, weights.split(' '))
numbers = map(int, number.split(' '))

nominator = 0
denominator = 0
# formula at work
for weight, number in zip(weights, numbers):
    denominator += number
    nominator += weight * number


    
print(round(nominator / denominator, 1))