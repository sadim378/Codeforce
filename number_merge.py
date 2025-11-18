t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    x = int(input())

    if n == 1:
        if arr[0] == x:
            print("YES")
        else:
            print("NO")
    else:
        found = False

        for i in range(n - 1):
            left = arr[i]
            right = arr[i + 1]

            if left <= x <= right:
                found = True
                break
            if right <= x <= left:
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")