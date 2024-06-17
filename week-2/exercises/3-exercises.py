sales = int(input("PLease enter the number of sales: "))
feedback_score = float(input("Please enter the feedback score out of 4.0 : "))


if sales > 100 and feedback_score >= 2.5:
    print("Performance: excellent")
elif sales > 100 or feedback_score >= 2.5:
    print("Performance: good")
else:
    print("Performance: needs improvement")