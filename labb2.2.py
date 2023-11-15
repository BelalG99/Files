def average(numbers):
    if not numbers:
        return 0  # Return 0 if the sequence is empty
    
    total = sum(numbers)
    num_count = len(numbers)
    avg = total / num_count
    return int(avg)  # Returning integer average

# Sample usage
print(average([1, 4, 4]))  # Output: 3
print(average([4, 4, 4, 4]))  # Output: 4
print(average([-2, 2]))  # Output: 0
