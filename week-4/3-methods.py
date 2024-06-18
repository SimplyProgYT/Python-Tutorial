# Removing items from a list

# Example list
fruits = ["apple", "banana", "strawberry"]

#! remove(), pop() and clear() methods

#? remove() method -> Removes a specific item

fruits.remove("banana")
print(fruits) # ['apple', 'strawberry']

#? pop() method -> Removing an item at a specific position
fruits.pop(0)
print(fruits) # ['strawberry']

#? clear() method -> Clearing the entire list
fruits.clear()
print(fruits) # []