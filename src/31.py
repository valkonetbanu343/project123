def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        if i > 1:  # add the square of each number greater than 1 to calculate the sum
            total += i * i
    return total

print(sum_of_squares(5))  # Example usage: Sum of squares up to 5
