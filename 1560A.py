t = int(input())

for i in range(t):
    k = int(input())
    count = 0 
    number = 0

    while count < k:
        number += 1

        if number % 3!= 0 and number % 10 != 3:
            count +=1


    print(number)