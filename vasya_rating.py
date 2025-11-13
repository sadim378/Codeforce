t = int(input())
for i in range(t):
    R0, X, D, n = map(int, input().split())
    rounds = input().strip()

    rating = R0
    count = 0

    for r in rounds:
        if r == '1':
            count += 1
            rating = max(0, rating - D)
        else:
            if rating < X:
                count += 1
                rating = max(0, rating - D)
            

    print(count)