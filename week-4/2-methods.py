# Adding items to a list

# Example list
fruits = ["apple", "banana"]

#! append(), insert() and extend() methods


#? append() method -> Adding an item to the end of the list

fruits.append("strawberry")
print(fruits) # ['apple', 'banana', 'strawberry']


#? insert() method  -> Inserting an item at a specific position

fruits.insert(1, "cherry")
print(fruits) # ['apple', 'cherry', 'banana', 'strawberry']
fruits.insert(3, "watermelon")
print(fruits) # ['apple', 'cherry', 'banana', 'watermelon', 'strawberry']

