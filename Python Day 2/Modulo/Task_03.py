numberStr = str(input("Enter your number\n"))

def SumOfDigit(number):
    result = 0
    for i in range(0, len(number)):
        digit = number[i]
        result += int(digit)
    print(result)

SumOfDigit(numberStr)