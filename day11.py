l1=[3,6,7,8,9]
l2=[45,76,87,90,123]
s=list(zip(l1,l2))
print("list1:",l1)
print("list2:",l2)
print("Merged list of tuples from l1 and l2:",s)

#2
l=[9,18,27,36,45]
r=list(range(1,9))
s=list(zip(1,r))
print("List:",l)
print("Range:",r)
print("Merged list of tuples from List and Range:",s)

#3
l=[67,98,57,83,27]
print("List before sorting:",l)
y=sorted(l)
print("List after sorting:",y)

#4
def evenfilter(x):
    if(x%2!=0):
        return True
    else:
        return False
l=[67,98,57,83,27]
print("List:",l)
y=list(filter(evenfilter,l))
print("List after filtering even numbers:",y)
