
# Create function that return Fibonacci Sequence
#
# Note:
#
# Do not use recursive

def calculate_fibo(n:int):
    """
    return fibonacci math row
    :param n: number of fibonacci elements
    :return: fibonacci row list
    """
    if n <= 0:
        return None
    else:
        fibo = [1, 1]
        if n < 3:
            return fibo[:n]
        else:
            for i in range(n-1):
                fibo.append(fibo[i] + fibo[i+1])
            return fibo