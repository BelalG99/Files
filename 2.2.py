def average(numbers):
    if not numbers:
        return 0  
    
    total = sum(numbers)
    num_count = len(numbers)
    avg = total / num_count
    return int(avg)  


print(average([1, 4, 4]))  
print(average([4, 4, 4, 4]))  
print(average([-2, 2]))  
