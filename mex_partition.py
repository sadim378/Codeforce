t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    count = [0] * 101
    for x in A:
        count[x] += 1

    mex1 = 0
    mex2 = 0

    for i in range(101):
        if count[i] == 0:
            mex1 = i
            break

    for i in range(101):
        if count[i] < 2:
            mex2 = i
            break

    print(mex1 + mex2)
