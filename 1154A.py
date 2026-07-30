numbers = list(map(int, input().split()))

numbers.sort()

total = numbers[3]

a = total - numbers[0]
b = total - numbers[1]
c = total - numbers[2]

print(a, b, c)