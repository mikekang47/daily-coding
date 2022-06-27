number = input()
result = 1
last = str
for i in range(len(number)):

    if i == 0:
        if number[i] == 'd':
            result *= 10
        else:
            result *= 26
        last = number[i]
    else:
        if last == number[i]:
            if number[i] == 'd':
                result //= 10
                result *= 90
            elif number[i] == 'c':
                result //= 26
                result *= 676-26
        else:
            if number[i] == 'd':
                result *= 10
            else:
                result *= 26
        last = number[i]
print(result)