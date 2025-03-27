#plp project python assignment second week

my_list = []
print(my_list)

#appending each value to the list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#result

print(my_list)

#appending 15 as the second element

my_list.insert( 1, 15)

#result 

print(my_list)

#extending my list with 50 70 and 80

my_list2 = [50, 70, 80]

my_list.extend(my_list2)

print (my_list)

#removing last element

my_list.pop()

print(my_list )

#sorting them on by one

for i in my_list:
	print (i)
	
#finding the index of  30
	
index = my_list.index(30)
	
print(index )