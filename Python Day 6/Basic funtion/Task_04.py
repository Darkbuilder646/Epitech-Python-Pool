def bread ():
    print (" <////////// > ")
def lettuce ():
    print (" ~~~~~~~~~~~~ ")
def tomato ():
    print (" O O O O O O ")
def ham ():
    print (" ============ ")

def MakeSandwiches(number: int, vegetarian: bool = False):
    if(number <= 0):
        print("I can't do this")
        return
    
    if(vegetarian == True):
        bread()
        tomato()
        tomato()
        lettuce()
        lettuce()
        bread()
        print("\n")
        return
    
    for i in range(number):
        bread()
        ham()
        ham()
        tomato()
        lettuce()
        bread()
        print("\n")

MakeSandwiches(2)
MakeSandwiches(3, True)