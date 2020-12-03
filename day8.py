#task1
# 1.index error
n = [1, 2, 3, 4]
try:
    a = int(input('enter the index num:'))
    print(n[a])
except IndexError:
    print('your enter index num is out of range:')
# 2.key error
D1 = {'1': "aa", '2': "bb", '3': "cc"}
try:
    print(D1['9'])
except KeyError:
    print('the key element is not found')
# 3.import error
import math

try:
    from math import cube
except:
    print('in math cube is not present')
# 4.value error
a = 'xyz'
try:
    print(int(a))
except:
    print('you entered A string is')
#task2
try:
    a = int(input('enter the number1:'))
    b = int(input('enter the number2:'))
    c = int(input('enter the operation:'))


    def operation(x, y):
        if c == 1:
            print(x + y)
        elif c == 2:
            print(x - y)
        elif c == 3:
            print(x * y)
        elif c == 4:
            print(x / y)
        else:
            print('the given operation is not defined')
    operation(a, b)
except(TypeError, ValueError, ZeroDivisionError, AttributeError, SyntaxError):
    print('something went wrong')
#task3
#type error
try:
    a=2+'2'
    print(a)
except TypeError:
    print('it is type error')
#name error
try:
    a='name'
    print(b)
except NameError:
    print('error occurred')
#task4
1 .try block runs the code and when there is no error tehn prints its code
2.whwn there is error occured in the code then exception block.
3.when no errors in the code we didnt want to use try-except scenario
