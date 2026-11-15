n = int(input())
a = list(map(int, input().split()))

programming = []
math = []
pe = []

for i in range(n):
    if a[i] == 1:
        programming.append(i + 1)
    elif a[i] == 2:
        math.append(i + 1)
    else:
        pe.append(i + 1)

teams = min(len(programming), len(math), len(pe))

print(teams)

for i in range(teams):
    print(programming[-teams + i], math[i], pe[i])