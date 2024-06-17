# Write a program that takes the bill amount and service quality as input and calculates the tip based on the service quality.

billAmount = float(input("Enter the bill amount: "))    
service_quality = input("Enter the service quality(excellent, good, fair, poor) :")

if service_quality == "excellent":
  tip_percentage = 0.20
elif service_quality == "good":
  tip_percentage = 0.15
elif service_quality == "fair":
    tip_percentage = 0.10
else:
  tip_percentage = 0.5
  
tip_amount = billAmount * tip_percentage

print("The tip amount is", str(tip_amount))