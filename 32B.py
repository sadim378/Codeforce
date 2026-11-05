s = input()

i = 0 
answer = ""

while i < len(s):
    if s[i] == ".":
        answer += "0"
        i += 1

    elif s[i:i+2] == "-.":
        answer += "1"
        i += 2

    else:
        answer += "2"
        i += 2

print(answer)