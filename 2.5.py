def string_with_numbers(n):
    result = '1'  # Start with a string containing '1'
    
    for i in range(2, n + 1):
        result += f'_{i}'  # Add underscores and the numbers from 2 to n
    
    return result

# Sample usage
print(string_with_numbers(3))  # Output: '1_2_3'
print(string_with_numbers(5))  # Output: '1_2_3_4_5'
