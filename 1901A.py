t = int(input())

for i in range(t):
    n, x = map(int, input().split())

    points = list(map(int, input().split()))
    maximum = points[0]

    for i in range(n - 1):
        distance = points[i + 1] - points[i]

        if distance > maximum:
            maximum = distance
    last_distance = (x - points[-1]) * 2
    if last_distance > maximum:
        maximum = last_distance

    print(maximum)