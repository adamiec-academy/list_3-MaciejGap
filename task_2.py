def fibonacci_sequence(n):
    result = []
    if n == 0:
        return result
    result.append(0)
    if n == 1:
        return result
    result.append(1)
    if n == 2:
        return result
    while len(result) != n:
        result.append(result[-1] + result[-2])
    return result
