age = int(input("Please enter your age: "))
day_of_week = input("Enter the day of the week: ").lower()

if age < 18:
    price = 60
elif age >= 65:
    price = 55
else:
    price = 75
    
# Check if it is a weekend

if day_of_week == "saturday" or day_of_week == "sunday":
    price += 10
    
# Print the ticket price

print("The ticket price:", price)