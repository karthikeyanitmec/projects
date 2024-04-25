
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


#multiple inheritance__________________-

# class skills():
#     def details(self,name="",exp=0,pov=0):
#         self.n=name
#         self.exp=exp
#         self.poc=pov
#     def print(self):
#         return self.n+" "+str(self.exp)+" "+str(self.poc)
# class additional():
#     def info(self,email="",skill=0):
#         self.em=email
#         self.sk=skill
#     def __str__(self):
#         return self.em+" "+str(self.sk)
# class checking(skills,additional):
#     def __init__(self,user,id=0,e=0,p=0):
#         super(checking,self),__init__(id,user,e,p)
#     def __str__(self):
#         return super(checking,self),__str__()+""+self.view()

# p=checking("karthi",5,23)
# print(p)


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


