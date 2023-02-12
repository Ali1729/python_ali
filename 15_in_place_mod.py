# example to demonstrate list is a mutable data type in python

# our current list
my_list = [1,2,3,4,5]
print(id(my_list))
# using append operation in our list
my_list.append(10)
# printing our list after the operation
print("List after appending a value = ",my_list)

# using extend operation in our list
my_list.extend([6,11,23])
print(id(my_list))
# printing our list after the operation
print("List after extending a list = ",my_list)

# after removing a value from our list
my_list.remove(3)
print(id(my_list))
# printing our list after the operation
print("List after removing a value = ",my_list)



# example to demonstrate 
# set is a mutable data type in python

# our current set
my_set = {1,2,6,5,7,11}

# adding an element in our set
my_set.add(16)
print(id(my_set))
# printing our set after the operation
print("Set after adding a value : ",my_set)

# adding multiple elements in our set
# multiple elements (such as a list) can be added using update
my_set.update([9,78,100])
print(id(my_set))
# printing our set after the operation
print("Set after updating some values : ",my_set)

# removing element from our set
my_set.remove(2)
print(id(my_set))
# printing our set after the operation
print("Set after removing a value : ",my_set)
