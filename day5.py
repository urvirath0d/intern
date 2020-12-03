def operations(a, b):
    sum1 = a + b
    sub1 = a - b
    mul1 = a * b
    div1 = a / b
    return sum1, sub1, mul1, div1


c = int(input("Enter the no "))
d = int(input("Enter the 2nd no "))
print(operations(c, d))


def covid(name, temp=98):
    print("enter the patients name", name)
    print("Patient body temperature is", temp)


covid("Urvi")
