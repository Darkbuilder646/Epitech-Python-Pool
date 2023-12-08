first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]

magic = [* zip( first_name , last_name [:: -1]) ]

print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

"""
On a deux list first_name et last_name
un créer un autre list magic 
qui permet de lié chaque élément de first_name avec last_name (last_name se lis dans l'autre sens)

magic [0] => élément 1 de first_name avec élément -1 de last name
magic [1][0] => print seulement l'élément 0 de l'élément lié 1
"""