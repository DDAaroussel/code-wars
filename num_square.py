#! python3

def square_digits(num):
    digits = list(map(int, str(num)))
    squared = [pow(x, 2) for x in digits]
    return squared
