#Task 1:Use math & statistics libraries to get square roots and average.
import math        # for square root
import statistics  # for average

# List of numbers
numbers = [4, 9, 16, 25, 36]

# Get square roots
square_roots = [math.sqrt(num) for num in numbers]

# Calculate average
average = statistics.mean(numbers)

# Print results
print("Original numbers:", numbers)
print("Square roots:", square_roots)
print("Average:", average)

