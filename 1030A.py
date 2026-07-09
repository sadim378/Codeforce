n = int(input())

response = map(int, input().split())

if 1 in response:
    print("HARD")
else:
    print("EASY")