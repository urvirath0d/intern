#Column 0 is the link
#Column 1 is the label 0-legitimate 1-malicious/phishing
#Column 2 is the length of link
#Column 3 is the number of /
#Column 4 is the number of digits
#Column 5 is the checking of www.

#Importing libraries
import pandas as pd
import re
import numpy as np

#Extracting dataset
data=pd.read_csv('urls.csv',engine="python")
data=data.iloc[:,[0,1,2,3,4,5]].values
l=len(data)

#Finding length
length=[]
for i in range(l):
    x=len(data[i][0])
    length.append(x)

for i in range(l):
    data[i][2]=length[i]

#Finding number of /,digits and presence of www.
slash=[]
digits=[]
for i in range(l):
    c=re.findall('/',data[i][0])
    d=re.findall('[0-9]',data[i][0])
    if(data[i][0].find('www.')!=-1):
        data[i][5]=1
    else:
        data[i][5]=0
    slash.append(len(c))
    digits.append(len(d))

for i in range(l):
    data[i][3]=slash[i]
    data[i][4]=digits[i]


#Independent and dependent variables
inde=data[:,[2,3,4,5]]
dep=data[:,1]

#Splitting train and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(inde, dep, test_size= 0.25, random_state=0)

#Decision Tree Classification
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(random_state = 0)
classifier.fit(x_train, y_train)

#Predicting test set
y_pred= classifier.predict(x_test)

#Obtaining Accuracy
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test,y_pred)

#Trying an example
link=input("Enter a link:")
a=len(link)
b=len(re.findall('/',link))
c=len(re.findall('[0-9]',link))
if(link.find('www.')!=-1):
    d=1
else:
    d=0
check=[a,b,c,d]
check=np.array(check)
check=check.reshape(1,-1)
find_it= classifier.predict(check)
find_it=int(find_it)
if(find_it==0):
    print("It is a legitimate link")
else:
    print("It is a malicious or a phishing link")
