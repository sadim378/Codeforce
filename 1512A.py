t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for j in range(n):
        if a.count(a[j]) == 1:
            print(j + 1)
            break