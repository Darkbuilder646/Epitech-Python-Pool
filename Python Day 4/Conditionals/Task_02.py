#odd => impaire 
#even = pair
number = int(input("Enter a integer\n"))

def isEven(value: int):
    return True if value % 2 == 0 else False

if(isEven(number)):
    print("This integer is even")
else:
    print("This integer is odd")