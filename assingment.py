
#ابراهيم محمد صلاح
# 1
a=[53,32,19,79,25,5,47]
min_=0
max_=0
for i in a:
 if i >max_:
   max_=i

   min_=max_
for i in a:
 if i <min_:
   min_=i

print(f"the maximum number is {max_}" )
print(f"the minimum number is {min_}")


# 2
a=int(input ("enter the first number"))
s=int(input ("enter the second number"))
if s%a==0 or a%s==0:
  print(True)
else:
  print (False)
# 3
s=input ("enter the variable is what")
print(type(s))
# 4
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]

for i in numbers:
 if i %2==0 :
   print (i)
 if i==237  :
   break;
# 5
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]
a=int(input("enter the number for check if the number in the group of values. "))
if a in numbers:
 print (True)
else:
 print (False)
# 6
sf=[1,2,3,3,3,4,5,5]
sd=[]
i=len(sf)
h=0
while h<i:
 if sf[h] not in sd:
  sd.append(sf[h])
 h+=1
print(sd)
# 7
str1=str(input ("enter string is paliendrome or not"))
str2=len(str1)
str2*=-1
str3=str1[-1:str2-1:-1]
if str3==str1:
 print("yes is paliendrome")
else:
 print("no is not paliendrome")
# 8
from math import *
g=int(input("ener the radius of the circle"))
print(factorial(g))
# 9
i=float(input("ادخل طول المستطيل"))
f=float(input ("ادخل عرض المستطيل"))
print(i*f)
# 10
i=float(input("ener the radius of the circle"))
print("the perimeter of the circle is",2*3.14*i)
print("the area of the circle is",3.14*i**2)



#ابراهيم محمد صلاح
