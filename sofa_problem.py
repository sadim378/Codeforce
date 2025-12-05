t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    never_ordered = []
    min_price = float('inf')

    for i in range(n):
        if a[i] > min_price:
            never_ordered.append(i + 1)
        else:
            min_price = a[i]

    print(len(never_ordered))
    if never_ordered:
        print(*never_ordered)
    else:
        print()
