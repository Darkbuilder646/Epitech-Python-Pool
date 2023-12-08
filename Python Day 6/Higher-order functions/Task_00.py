specialChar = '[@_!#$%^&*()<>?/\|}{~:]'

def funA (s: str, n: int):
    count = 0
    for char in s:
        if(char.islower()):
            count += 1
    if(count >= n):
        return True
    else:
        return False
    
def funB (s: str, n: int):
    count = 0
    for char in s:
        if(char.isupper()):
            count += 1
    if(count >= n):
        return True
    else:
        return False

def funC (s: str, n: int):
    count = len(s)
    if(count >= n):
        return True
    else:
        return False

def funD (s: str, n: int):
    count = 0
    for char in s:
        if(char in specialChar):
            count += 1
            print(count)
    if(count >= n):
        return True
    else:
        return False

def funE (s: str, n: int):
    count = 0
    for char in s:
        if(char.isnumeric()):
            count += 1
    if(count >= n):
        return True
    else:
        return False

print(funA("Hello", 2))
print(funB("Hello", 2))
print(funC("Hello", 4))
print(funD("Hello%", 1))
print(funE("Hello123", 3))
