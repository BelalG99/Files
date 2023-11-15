def sum_of_ints(seq1, seq2):
    total_sum = sum(seq1) + sum(seq2)
    return total_sum

# Sample usage
print(sum_of_ints([1, 4, 2], [2, -1]))  # Output: 8
print(sum_of_ints([4, 4, 4, 4], []))  # Output: 16
print(sum_of_ints([4, 4], [4, 4]))    # Output: 16
