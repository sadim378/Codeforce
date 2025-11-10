t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    has_evan = any(x % 2 == 0 for x in a)
    has_odd = any(x % 2 == 1 for x in a)

    if has_evan and has_odd:
        a.sort()

    print(*a)