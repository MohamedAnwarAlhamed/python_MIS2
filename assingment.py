
#احمد عبدالله الدعيس
# 1
a=[53,32,19,79,25,5,47]

print(max(a))
print("-----------------")
print(min(a))

# 2
a=int (input("enter number 1: "))
b=int (input("enter number 2: "))

c=a/b
if a%b==0:
    print(True)
elif a%b==1:
    print(False)
# 3
a=[]

print(type (a))
# 4
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]
for i in numbers:
    if i%2==0:
        print(i)
        if i ==237:
            break

# 5
a=int (input("enter number:"))
group=[1,5,8,3,3]
if a in group:
    print(True)
else:
    print(False)
# 6
a=[1,2,3,3,3,3,4,5]
print(set(a))
# 7
a=input("enter:")

x=""
z=len(a)
for i in a:
    x+=a[z-1]
    z=z-1
d=x
print(d)
if d==a:
    print(True)
else:
    print(False)
# 8
num= int (input("enter number"))
md=1
for i in range(1,num+1):
    md=md*i
    print(md)
# 9
z=int
w=int
print ("لحساب مساحة المستطيل اضغط الرقم 1 :")
print ("لحساب محيط المستطيل اضغط الرقم 2 :")
z=int (input("ادخل رقم العملية:"))
if (z==1):
  x=int (input("ادخل طول المستطيل:"))
  y=int (input("ادخل عرض المستطيل:"))
  print ("مساحة المستطيل =",x*y)
if (z==2):

  x = int(input("ادخل طول المستطيل:"))
  y = int(input("ادخل عرض المستطيل :"))
  w =2*(x+y)
  print("محيط المستطيل = ",w)
# 10
radius = int(input("Enter the radius of a circle"))
area = 3.1415 * radius * radius
cir = 2 * 3.1415 * radius
print(f"Area = {area} and Circumference = {cir}")


#احمد عبدالله الدعيس
