numberStr = str(input("Enter your number\n"))

def ExtractFloatDigit(number):
    result = ""
    for i in range(0, len(number)):
        if(number[i] == "."):
            result = ""
        digit = number[i]
        result += digit
    print(result)

ExtractFloatDigit(numberStr)

"""
n=str(input())
def E(n):
    r=""
    for i in range(0, len(n)):
        if(n[i]=="."):
            r=""
        d=n[i]
        r+=d
    print(r)
E(n)
"""