# 1
original_1st = list([1, 2, 3, 4])
print(original_1st)
new_1st = [x + 2 for x in original_1st]
print(new_1st)
# 2
p = 5
for i in range(p):
    for j in range(p):
        temp = p - j
        print(temp, end="")
    print()
    p -= 1
# 3
a = 0
b = 1
n = 10
sum1 = 0
while sum1 <= n:
    print(sum1)
    a = b
    b = sum1
    sum1 = a + b
# 4
for i in range(11):
    ans = 9 * i
    print(ans)
# 5
ans = int(input("enter the number of days :"))
a = int(ans / 365)
print("number of years is :", a)
# 6
import math

a = math.pi / 6
print("the value of sin pi/6 is :", end="")
print(math.sin(a))
# 7
print('1.ADDITION\n2.SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION')
cal = int(input("Enter the choice you want to enter : 1 to 4"))
if cal == 1:
    a = int(input("1st number:"))
    b = int(input("2nd number"))
    ans = a + b
    print("Addition =", ans)
elif cal == 2:
    a = int(input("1st number:"))
    b = int(input("2nd number"))
    ans = a - b
    print("Subtract = ", ans)
elif cal == 3:
    a = int(input("1st number:"))
    b = int(input("2nd number"))
    ans = a * b
    print("Multiply = ", ans)
elif cal == 4:
    a = int(input("1st number:"))
    b = int(input("2nd number"))
    ans = a / b
    print("Divide = ", ans)
else:
    print("You have made an invalid choice")


#
def armstrong(number):
    count = 0
    num = number
    while num != 0:
        num = num % 10
        count += 1
    expo = count
    while num != 0:
        base = num / 10
        tem = 1
        add = 0
        for x in expo:
            tem = tem * base
            add = add + tem
    if add == number:
        print("Armstrong Number")


c = int(input("enter the number:"))
print(armstrong(c))
