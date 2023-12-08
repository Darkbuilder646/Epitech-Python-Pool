key = str(input("Enter your Vigenere Key\n")).lower()
string = str(input("Enter your text to encrypt\n")).lower()
cryptString = ""

def Encrypt(stringToEncrypt: str, outputString:str, key: str):
    for i in range(len(stringToEncrypt)):
        index = (ord(stringToEncrypt[i]) + ord(key[i])) % 26
        outputString += chr(97+index)

    return outputString

print(Encrypt(string, cryptString, key))
