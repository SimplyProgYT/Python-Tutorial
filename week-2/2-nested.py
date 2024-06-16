# Nested statements syntax

temperature = 30
humidity = 75

if temperature > 25:
    if humidity > 60:
        print("It is hot and humid today")
    else:
        print("It is hot today but not too humid")
else:
    if humidity > 60:
        print("It is cool but humid today")
    else:
        print("It is cool and dry today")