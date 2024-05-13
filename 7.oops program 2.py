#polymorphism____________

# class birds:
#     def coc(self):
#         print('cockooo')
#     def parrot(self):
#         print('kiii kiii')
# class birds2(birds):
#     def peacock(self):
#         print('meow')
    
# class birds3(birds):
#     def lovebirds(self):
#         print('kitch kitch')

# o1=birds2()
# o1.peacock()
# o1.coc()

# o2=birds3()
# o2.lovebirds()
# o2.parrot()

#poly overriding______

# class sam:
#     def name(self):
#         print('first name')

# class ram(sam):
#     def name(self):
#         super().name()
#         print('second name')

# class kiran(ram):
#     def name(self):
#         super().name()
#         print('third name')

# k=kiran()
# k.name()
# print(k)



#overridding_____-

# class sam:
#     def name(self,a):
#         print(a)
#     def name(self,a,b):
#         print(a+b)
#     def name(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.name(1,2,3)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# obj=over()

# print('sam',obj.load(10))
# print('ram',obj.load(10,20))
# print('karthi',obj.load(10,20,30))


#multiple args____

# class multiple:
#     def add (self,*args):
#         sum=40
#         for i in args:
#             sum+=i
    
#         print('total values',sum)

# c=multiple()
# c.add(10)
# c.add(10,20)
# c.add(10,20,30,30,49)
# c.add(233,1334,12243,133)

#operator overloading____

# class operator:
#     def __init__(self,a):
#         self.a=a

#         print(self.a+self.a)

# o=operator(10)
# o1=operator(20)
# print("sum",o.a+o1.a)



# class operator:
#     def __init__(self,a):
#         self.a=a
    
#     def __add__(self,b):
#         return self.a+b.a
    
# o=operator(10)
# o1=operator(20)
# print("sum",o+o1)
