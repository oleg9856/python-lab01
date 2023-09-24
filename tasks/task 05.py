
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print('Number: ')
    n = int(input())
    print('The factorial of', n, 'is', factorial(n))
