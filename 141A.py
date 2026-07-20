guest = input()
host = input()
pile = input()

combine = guest + host

if sorted(combine) == sorted(pile):
    print("YES")
else:
    print("NO")