
#المعتصم بالله القدمي##
# 1
a=[47,5,25,79,19,32,53]
print("min,mix")
print(max(a))
print(min(a))

# 2
e=int(input("Entr the nampr"))
s=int(input("Entr the nampr"))
if e%s==0:
    print(True)
else:
    print(False)
# 3
a=input("لمعرفه ماهواادخل اي شي ")
if a==str:
    print("string")
elif a==float:
    print("flot")
elif a==int:
    print("intgar")
# 4
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]
for i in numbers:
    if i%2==0:
        print(i)
        if i ==237:
            break

# 5
a=[3,3,8,5,1]
p=int(input("ادخل رقم لمعرفه هل يوجد بالمصفوفه"))
if p in a:
   print(True)
else:
   print(False)
# 6
a=[1,2,3,3,4,4,5]
p=[]
for o in a:
    if o not in p :
       p.append(o)
print(p)
# 7
e = str(input("ادخل كلمه اذا عكستها تكون نفس الكلمه  "))
p = len(e)
c = ""
while p > 0:
    c += e[p - 1]
    p -= 1

if c == e:
    print("Truo")
else:
    print(False)
# 8
i=int(input("لمعرفه مضروب العدد"))
v=1
s=1
while v<=i:
  s*=v
  v+=1
print(s)
# 9
t=int(input("ادخل طول المستطيل"))
q=int(input("ادخل عرض المستطيل"))
m=t*q
print("مساجه المستطيل =")
print(m)
# 10
r=int(input("لمعرفه ناتج محيط ومساحه الداءره"))
m=float
m=3.14*2*r
print("مساحه =")
print(m)
h=3.14*r*r
print("المحيط=")
print(h)


#المعتصم بالله القدمي
