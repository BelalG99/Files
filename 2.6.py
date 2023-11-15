def xxx(n):
    total_sum = 0
    
    for i in range(1, n + 1):
        for j in range(i):
            total_sum += i
            
    return total_sum

# Sample usage
print(xxx(1))  # Output: 1
print(xxx(2))  # Output: 5
print(xxx(3))  # Output: 14
print(xxx(4))  # Output: 30
