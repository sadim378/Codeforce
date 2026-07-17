n, m = map(int, input().split())

right  = True

for row in range(1, n + 1):

    if row % 2 == 1:
        print("#" * m)
    else:
        if right:
            print("." * (m - 1) + "#")
            right = False
        else:
            print("#" + "." * (m - 1))
            right = True