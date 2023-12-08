numberStr = str(input("Enter your number\n"))

def ExtractIntegerDigit(number):
    result = ""
    for i in range(0, len(number)):
        if(number[i] == "."):
            break
        digit = number[i]
        result += (digit)
    print(result)

ExtractIntegerDigit(numberStr)