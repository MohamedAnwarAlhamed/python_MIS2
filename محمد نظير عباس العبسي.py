#(1)##
# c=[53,32,19,79,25,5,47]
# x=min(c)
# y=max(c)
# print(f"min={x}")
# print(f"max={y}")
#(2)#############################
# x=int (input("enter the number 1:"))
# y=int (input("enter the number 2:"))
# if x % y==0:
#     print("True")
# else:
#     print("false")
#(3)########################################
# y =[4,5,7,9,4,3,6,7]
# print(set(y))
# print(type(y))
#(4)###################################
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 
#  758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 
#  58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]
# for number in numbers:
#     if number%2==0:
#       print(number)
#       if number == 237:
#        break
#(5)################################################
# x =int(input("enter the number :"))
# g =[1,5,8,3,4]
# if x in g:
#     print(True)
# else:
#     print(False)
#(6)####################################
# a =[1,2,3,3,3,4,5,3,6]
# print(set(a))
#(7)#################################################
# y =input("enter the word :")
# a =""
# x =len(y)
# for b in y :
#     a+=y[x-1]
#   #  print(a)
#     x=x-1
# f=a
# print(f)
# if f == y:
#     print(True)
# else:
#     print(False)
#(8)#####################################
# a =int(input("enter the number + :"))
# x =1
# for y in range(1,a+1):
#     x =x*y
#     print(x)
#(9)######################################
# class squr1:
#     def __init__(self,l,w):
#      self.l= l
#      self.w= w
#     def area_r (self,l,w):
#         x=l*w
#         return x
#     def mohit(self,l,w):
#         mo =2*(l+w)
#         return mo
# l1=int(input("input the langth:"))
# w1=int(input("input the width:"))
# y=squr1(l1,w1)
# print("area =",y.area_r(l1,w1))
# print("mohit =",y.mohit(l1,w1))
#(10)###################################################
# p=3.14
# class crc:
#     def __init__(self,p,r):
#      self.p= p
#      self.r= r
#     def area_r(self,p,r):
#      b=p*r*r
#      return b
#     def mohit(self,p,r):
#         mo =2*p*r
#         return mo
# p=3.14
# r11=float(input("input the radius:"))
# ww=crc (p,r11)
# print("area circle =", ww.area_r(p,r11))
# print("mohit circle=", ww.mohit(p,r11))
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&