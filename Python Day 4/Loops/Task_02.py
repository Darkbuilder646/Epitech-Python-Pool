def DivideBySeven(number: int):
    return True if number % 7 == 0 else False
i = 10000
while i >= 1:
    if(DivideBySeven(i)):
        print(i)
    i -= 1