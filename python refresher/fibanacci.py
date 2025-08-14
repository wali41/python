
# to print a fibonacci series

def fibonacci_series(n):

    a, b = 0, 1

    series = []

    for _ in range(n):

        series.append(a)

        a, b = b, a + b
    return series
    




# Example usage

print(fibonacci_series(10))