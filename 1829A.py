t = int(input())

for i in range(t):
    s = input()

    target = "codeforces"

    count = 0

    for j in range(10):
        if s[j] != target[j]:
            count += 1

    print(count)