# 4 = 4 * 3 * 2 * 1 = 25
def fatorial(n):
    if n == 1 or n == 0:
        return 1

    return n * fatorial(n - 1)


if __name__ == "__main__":
    print(fatorial(10))
