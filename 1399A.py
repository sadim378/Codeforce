t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    possible = True

    for j in range(n - 1):
        if a[j + 1] - a[j] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")