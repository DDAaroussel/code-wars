#! python3

def series_sum(n):
    if n == 0:
        sum = 0
        sum1 = format(sum, '.2f')
        return str(sum1)
    else:
        sum = 0
        for i in range(1,n+1):
            sum = sum + (1/(i*3-2))
        sum1 = format(sum, '.2f')
        return str(sum1)
