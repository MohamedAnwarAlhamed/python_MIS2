# print(" برنامج يوجد الرقم الاكبر والرقم الاصغر من دون استخدام الدوال")
# def largest_number(list):
#     f = list [0]
#     for a in list:
#         if a> f:
#             f = a
#     return f
# print ( largest_number([53,32,19,79,25,5,47]))

# def smallest_number(list):
#     w = list [0]
#     for a in list:
#         if a< w:
#             w= a
#     return w
# print (smallest_number([53,32,19,79,25,5,47]))

###############################
#print("برنامج يخبرك ان العدد المدخل يقبل القسمه ام لا")
# def divisible(a,b):
#     if a%b==0:
#         print("number is divisble : true")
#     else:
#             print("number is not divisble  :false ")

# a= int (input("Enter the number :"))
# b=int((input("Enter the number :")))
# divisible(a,b)
###############################
# print("jjjj")
# a=[2]

# print(type(a))
################################
# print("برنامج طباعه جميع الارقام الزوجيه من قايمه الارقام وتتوقف عندما يصل الى237")
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248,866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,843, 831, 445, 742, 717,958,743, 527]

# for i  in numbers:
#     if i==237:
#         break
#     elif i % 2 == 0:
#         print(i)
#################################
# print("برنامج يتحقق مما اذا كانت القيمه موجوده في المجموعه من القيم")
# a=int(input("enter the numbers :"))
# c =[1,5,8,3,3]
# if a in c :
#     print("true")
# else :
#     print("false")
################################
# print( دون استخدام داله تاخذ قاىمه وتعيد قاىمه جديده )
# def unique_list(l):
#   x = []
#   for a in l:
#      if a not in x:
#          x.append(a)
#   return x

# print(unique_list([1,2,3,3,3,3,4,5]))
##############################
# print(استخدمنا دالهpalindrome تاخذ المدخلات وتعيده اذا كانت السلسه متناضره)
# def ispalindrome(s):
#     return s == s[::-1]

# s = "malayalam"
# ans = ispalindrome(s)

# if ans:
#     print("yes")
# else:
#     print("no")
################################
#***** print('كتابه داله لحساب مضروب العدد المدخل  اذا كان العدد  ويكون عدد صحيح غير سالب' )

# def factorial(n): 
#     if n == 0 :
#       return 1 
#     else:
#      print ("the number is not positivr")
# n=int(input("Input  a number to compute the  factiorial :"))
# print(factorial(n))
###############################
# print ("برنامج يقوم بعداد نسخه و  ويوجد مساحه المستطيل ")
# class Rectangle:
#     def __init__(self ,length ,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length*self.width
# Rectangle =Rectangle(10, 20) 
# print(Rectangle.area)      
################################
# print("برنامج يقوم   بطلب من المستخدم ادخال  نصف قطر الداىره ةيقةم بحساب  مساحته ومحيط الداىره")
# class circle :
#     def ___intit___(self,ss) :
#         self.ss =ss
#     def area (self):
#         return self.ss**2*3.14
#     def perimenter (self):