t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    seen = set()
    total = 0

    for ch in seen:
        if ch not in seen:
            total += 2
            seen.add(ch)
        else:
            total += 1

    print(total)