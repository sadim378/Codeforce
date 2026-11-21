t = int(input())

for i in range(t):
    b  =input()
    a = ""

    for j in range(0, len(b), 2):
        a += b[j]

    a += b[-1]

    print(a)