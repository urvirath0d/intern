#1
string=input("Enter a string:")
if(re.match('^[a-zA-Z0-9]*$',string)):
      print("the string is valid!")
else:
      print("The string is not valid!")
#2
values=['sun','tab','above','bat','author']
print("List contains:",values)
print("Words in the list containing 'ab':",end=' ')
for i in values:
    if(re.search('ab',i)):
        print(i,end=' ')
