def is_perfect(n):
    divisor_sum = 0
    for a in range(1, n):
        if n % a == 0:
            divisor_sum = divisor_sum + a
    if divisor_sum == n:
        return True
    return False


def get_perfect_numbers(n):
    result = []
    z = 1
    while len(result) != n:
        if is_perfect(z):
            result.append(z)
        z = z + 1
    return result

