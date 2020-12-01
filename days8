#1
a=lambda x,y : x*y
print(a(9,2))
#2
n = int(input('enter the no'))
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                              range(n - 2), [0, 1])
print(fib_series(n))
#3
a=[1,2,3,4]
n = int(input('enter the number:'))
multiply_list=list(map(lambda number:number*n,a))
print(multiply_list)
#4
a=[1,2,3,4]
result=list(filter(lambda x: (x % 9 == 0), a))
print(result)
#5
a=[1,2,3,4,5,6,7,8,9]
even_nos = len(list(filter(lambda x : (x%2 == 0) , a)))
print(even_nos)
