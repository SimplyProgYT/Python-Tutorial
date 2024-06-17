# Write a program that takes the current color of a traffic light as input and prints the action a driver should take.

# Take the current color of the traffic light from the user
lightColor = input("Please enter the traffic light color (red, green or yellow): ").lower()

if lightColor == "red":
    print("Stop!")
elif lightColor == "yellow":
    print("Caution. Prepare to stop.")
elif lightColor == "green":
    print("Go!")
else:
    print("Invalid color entered.")