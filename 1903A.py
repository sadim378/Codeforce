t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    boxes = list(map(int, input().split()))

    if k >= 2:
        print("YES")
    else:
        if boxes == sorted(boxes):
            print("YES")
        else:
            print("NO")