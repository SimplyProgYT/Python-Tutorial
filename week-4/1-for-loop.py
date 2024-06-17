# for loop syntax

sum = 0

""" for i in range (1, 11):
    sum += i
print("1 + 2 + 3... + 10 =", sum)
 """
for i in range(1, 11):
    if i % 2 == 0:
        sum += i

print(sum)