# Adding items to a list

# Example list
fruits = ["apple", "banana"]

#! append(), insert() and extend() methods


#? append() method
fruits.append("strawberry")
print(fruits) # ['apple', 'banana', 'strawberry']


#? insert() method  

fruits.insert(1, "cherry")
print(fruits) # ['apple', 'cherry', 'banana', 'strawberry']
fruits.insert(3, "watermelon")
print(fruits) # ['apple', 'cherry', 'banana', 'watermelon', 'strawberry']