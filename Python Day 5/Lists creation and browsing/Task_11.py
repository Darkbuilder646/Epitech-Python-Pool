my_first_list = [4,5,6]
my_second_list = [1,2,3]
my_first_list.extend(my_second_list)
#.extend() permet d'ajouter les élement d'une list à une autre
print(my_first_list)

my_first_list2 = [7,8,9]
my_second_list2 = [4,5,6]
my_first_list2 = [*my_first_list2, *my_second_list2]
#Remplace chaque élément de la list 1 par l'élément de la list 2 pour le même index
print(my_second_list2)