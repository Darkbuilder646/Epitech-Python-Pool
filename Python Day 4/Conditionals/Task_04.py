number = int(input("Enter a integer\n"))

def isEven(value: int):
    return True if value % 2 == 0 else False

if(number == 42):
    print("OK")
elif(number <= 21):
    print("OK")
elif(isEven(number)):
    print("OK")
elif((number / 2) < 21):
    print("OK")
elif(isEven(number) != True and number >= 45):
    print("OK")
else:
    print("You got wrong my poor friend!")