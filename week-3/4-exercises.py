overdue_days = int(input("Enter the number of overdue days: "))
book_type = input("Enter the book type (regular or new release): ").lower()

regular_fee_per_day = 0.25
new_release_fee_per_day = 0.50

if book_type == "regular":
    late_fee = overdue_days * regular_fee_per_day
elif book_type == "new release":
    late_fee = overdue_days * new_release_fee_per_day
else:
    late_fee = None
    
if late_fee is not None:
    print("The late fee is", late_fee)
else:
    print("Invalid book type entered.")