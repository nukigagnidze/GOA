def odd_index_sum(numbers):
    total = 0
    for index in range(1, len(numbers), 2):  
        total += numbers[index]
    return total