string1 = "kayak"
string2 = "never odd or even"
string3 = "Was it a car or a cat i saw?"

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def AdapteString(string: str):
    for char in string:
        if char in punc:
            string = string.replace(char, "")
    string = "".join(string.split()).lower()
    return string

def IsPalindrome(string: str):
    string = AdapteString(string)
    if(string == string[::-1]):
        return True
    else:
        return False

print(IsPalindrome(string1))
print(IsPalindrome(string2))
print(IsPalindrome(string3))