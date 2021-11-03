#summary to lists, tuples and their functions etc.
my_list = ['string_1', 'string_2', 'string_2', 11, 22, 33, 44]
my_tuple = ('value_1', 'value_1', 'value_2', 3, 4)
tuple_to_unpack = ('one', 'two', 'three')

#------list manipulations------
print('\n[------Console logs for lists section------]\n')
print('------items and typeof------')

for item in my_list: #print type of every list item before modifications
    print(str(item) + ' is ' + str(type(item)))

print('\n------slices------')
print(my_list[1]) #get the 2-nd element of the list (by index)
print(my_list[-1]) #get the last element of the list 
print(my_list[2:]) #get all the elements of the list starting from the third one
print(my_list[1:4]) #get all the elements starting from the 2-nd element (included) & till the 4-th one 
print(my_list[::2]) #print the list items from the beginning to the end with a step
#
# if we want to access list element by value
# print(type(my_list['string_1'])) causes the following error:
# TypeError: list indices must be integers or slices, not str
#
my_list.append('new_string_1') #add one element to the list
my_list.remove('string_2') #removes the first occurence of the given value 
list_copy = my_list.copy() #though it creates a shallow copy, it can't modify the orignal list
list_copy.append('i_hacked_the_list')

print('\n------after modifications------')
print(my_list) #print the list after modifications
print(list_copy) #comparison with the copied list


#------tuple manipulations------
print('\n\n[------Console logs for tuples section------]\n')
print(my_tuple)
print(my_tuple[:-1]) #every value except the last one
print(my_tuple[2]) #print the 3-rd value

#add new values by adding 2 tuples
tup_add_val = ('add_this_1', 'add_this_2')
my_tuple += tup_add_val
print(my_tuple)

#modify by converting tuple to list 
buff_tup_to_list = list(my_tuple)
buff_tup_to_list.append('hack_1')
buff_tup_to_list.remove('add_this_2')
my_tuple = tuple(buff_tup_to_list)
print(my_tuple)

#unpacking (converting tuple values to variables); doesn't work with tuples
#with multiple data types within
(val_1, val_2, val_3) = tuple_to_unpack 
print(val_1)
print(val_2)
print(val_3)