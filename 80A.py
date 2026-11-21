n, m = map(int, input().split())

for num in range(n + 1, m + 1):
    prime = True

    for j in range(2, num):
        if num % j == 0:
            prime = False
            break

    if prime:
        if num == m:
            print("YES")
        else:
            print("NO")

        break
else:
    print("NO")