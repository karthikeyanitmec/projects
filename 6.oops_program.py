
# #program single inheritance example_________

# class Account():
#     accountno=0
#     accountbal=0
#     accountholder=""
#     def __str__(self):
#         return str(self.accountno)+" "+self.accountholder+" "+str(self.accountbal)+"\n"

# class Card(Account):
#     cardnumber=0
#     def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
#         self.cardnumber=cn
#         self.transaction=[]
#         self.accountno=anum
#         self.accountholder=ahold
#         self.accountbal=abal
#     def __add__(self,amt):
#         self.accountbal+=amt
#         print(amt,"is deposited",self.accountholder)
#         self.transaction.append('credit')
#     def __sub__(self,draw):
#         if self.accountbal>=draw:
#             self.accountbal-=draw
#             print(draw,'is withdraw',self.accountholder)
#             self.transaction.append('debit')
#         else:
#             print("Insufficient balance")
#     def countTrans(self):
#         crecount=self.transaction.count('credit')
#         debcount=self.transaction.count('debit')
#         charge=0
#         if crecount>=5:
#             charge+=(crecount-5)*10
#         if debcount>=3:
#             charge+=(crecount-3)*20
#         print("total charge on transaction count is",charge)
#         self.accountbal-=charge
#     def __str__(self):
#         return str(super(Card,self).__str__())+"\n"+str(self.cardnumber)+" "+str(self.accountbal)+"\n"

# a1=Account()
# a1.accountno=1234567
# a1.accountholder="karthi"
# a1.accountbal=25000
# print(a1)


# c1=Card(1233445,12334,"keyan",2000)
# c1+1000
# print(c1)
# c1-100
# print(c1)
# c1+100
# c1-200
# c1+1000
# c1+100
# c1-100
# c1+100
# print(c1)
# c1.countTrans()





#multilevel inheritance______________


# class college:
#     def studentinfo(self):
#         self.roll_no=input("enter your rollno:")
#         self.name=input("enter your name:")
#     def printstudentinfo(self):
#         print('rollno:',self.roll_no,"name:",self.name)
# class BE(college):
#     def getmarks(self):
#         self.studentinfo()
#         self.__m=int(input('enter your maths mark:'))
#         self.__p=int(input('enter your physics mark:'))
#         self.__b=int(input('enter your biology mark:'))
#     def printmarks(self):
#         self.printstudentinfo()
#         print('list of marks:',self.__m,self.__p,self.__b)
#     def totalmarks(self):
#         return (self.__m+self.__p+self.__b)
# class result(BE):
#     def gresults(self):
#         self.getmarks()
#         self.__total=self.totalmarks()
#     def presults(self):
#         self.printmarks()
#         print("total marks of 300:",self.__total)

# c=result()
# c.gresults()
# c.presults()


#multiple inheritance__________________


# class SkillSet:
#     def __init__(self,name="",exp=0,poc=0):
#         self.skill=name
#         self.exp=exp
#         self.poc=poc
#     def view(self):
#         return self.skill+" "+str(self.exp)+" "+str(self.poc)


# class Personal:
#     def __init__(self,name,qual="",con=0,mail=""):
#         self.name=name
#         self.qualification=qual
#         self.contact=con
#         self.mail=mail
#     def __str__(self):
#         return self.name+" "+self.qualification+" "+str(self.contact)+" "+self.mail

# class Profile(Personal,SkillSet):
#     def __init__(self,user="",q="",c=0,m="",s="",e=0,p=0):
#         super(Profile, self).__init__(user,q,c,m)
#         self.skill=s;self.exp=e;self.poc=p
#     # def __str__(self):
#     #     return super(Profile, self).__str__()+" "+self.view()

# pro=Profile("saran","IT",78458956,"saran@gmail.com","python Backend",5,2)
# pro1=Profile("karthi","It",785522,"karthi@gmail.com","Python and Java")
# print(pro)
# print(pro1)

#encapsulation______________


# class mobiles:
#     __model=""
#     __ram=0
#     __price=0
#     def setmodel(self,mod=""):
#         self.__model=mod
#     def getmodel(self):
#         return self.__model
#     def setram(self,rams=""):
#         self.__ram=rams
#     def getram(self):
#         return self.__ram
#     def setprice(self,pri=""):
#         self.__price=pri
#     def getprice(self):
#         return self.__price
# m=mobiles()
# m.setmodel("redmi")
# m.setram(8)
# m.setprice(10000)
# print(m.getmodel(),m.getram(),m.getprice())


#hybrid inheritance_________________

# class college:
#     def name(self,totals,total):
#         self.staffs=int(input("sjc"))
#         self.students=int(input("sjcssd"))

# class staff(college):
#     def totalstaffs(self):


# class student(college):
#     def total(self):
#         self.name()

# class salary(staff,student):
#     def calculate(self,add=""):
#         self.add=str(self.totalstaffs)+str(self.total)

# o=salary()
# o.calculate()



# example 2

# class operators:
#     def inputs(self):
#         self.a=int(input('value a'))
#         self.b=int(input('value b'))

# class addition(operators):
#     def add(self):
#         self.inputs()
#         total=self.a+self.b
#         print("addition",total)


# class subraction(operators):
#     def sub(self):
#         self.inputs()
#         total=self.a-self.b
#         print("subtraction",total)

# class final(addition,subraction):
#     def results(self):
#         self.add()
#         self.sub()

# r=final()
# r.results()


#hierarical inheritance_____


# from array import *

# class stocks:
#     products=array('i')
#     def pro(self):
#         print('products are',self.products)

# class pothys(stocks):
#     def __init__(self,store):
#         self.products=array('i')
#         self.products.extend(store)
    
#     def search(self):
#         budget=int(input('enter your search'))
#         for x in self.products:
#             if x<=budget:
#                 print(x)
# class reliance(stocks):
#     def __init__(self,st):
#         self.products=array('i')
#         self.products.extend(st)
#     def print(self,start,stop):
#         print(self.products[start:stop])
# p=pothys([5,4,3,2])
# r=reliance([233,123,234,23,23])

# p.search()
# r.print(0,3)
# r.pro()
# p.pro()


# abstraction______

# from abc import *

# class falcon(ABC):
#     def __init__(self):
#         self.mine={43,12,4,5,6,666,77,78}
#     def heythere(self):
#         pass

# class passed(falcon):
#     def there(self):
#         print(self.mine)


# p=passed()
# p.there()


#constructors_________

# class Account:
#     def __init__(self,name="",bal=0,num=0):
#         self.__holder=name
#         self.__balance=bal
#         self.__accno=num
    
#     def __add__(self,other):
#         self.__balance+=other
#         print(other,'credited',self.__balance)
#     def __sub__(self,other):
#         if self.__balance>=other:
#             self.__balance=other
#         else:
#             print(self.__balance,'insufficient balance')

#     def __str__(self):
#         return self.__holder+" "+self.__balance+""+self.__accno
    
#     def setholder(self,name=""):self.__holder=name
#     def getholder(self):return self.__holder
#     def setbalance(self,bal=0):self.__balance=bal
#     def getbalance(self):return self.__balance
#     def setaccno(self,num=0):self.__accno=num
#     def getaccno(self):return self.__accno

# a=Account()
# a.setaccno(12344)
# print(a.getaccno())
# a.setholder("karthi")
# print(a.getholder())
# a.setbalance(1000)
# print(a.getbalance())
# a+=500
# print(a)


