def f(x):
    return 2 * x + 1
def g():
    return 7

y = f(2)
print (y)
y = f(5) + g()
print (y)


"""
La fontion f(x) retourne 2*x+1
Donc pour y = f(2) => 2*2+1 => 5
g() retourne seulement 7
Donc f(5) + g() = 2*5+1 + 7 => 18
"""