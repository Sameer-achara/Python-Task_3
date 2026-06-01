from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

evens = list(filter(lambda x: x % 2 == 0, numbers))

total = reduce(lambda x, y: x + y, numbers)

print("Original:", numbers)
print("Squares:", squares)
print("Even Numbers:", evens)
print("Sum:", total)
