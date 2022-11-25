def tower(n):

    total_width = 2 * n - n

    for i in range(1, n + 1):
        current_width = 2 * i - 1
        for _ in range(3):

            print((total_width - 1 * i) * " " + (2 * i - 1) * "#" + (total_width - 1 * i) * " ")


def towers(data):
    pass
