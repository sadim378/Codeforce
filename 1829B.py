t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    current = 0
    maximum = 0

    for x in arr:
        if x == 0:
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    print(maximum)