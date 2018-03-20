def recurs(n):
    if n > 0:
        print(n)
        n * recurs(n - 1)
        return 0
    else:
        return 1

print(recurs(10))