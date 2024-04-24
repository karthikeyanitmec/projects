# class college:
#     def __init__(self,name,course):
#         self.n=name
#         self.c=course
#     def print(self):
#         print(self.n,self.c)
# c=college("karthi","IT")
# c.print()

# class karthi:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def output(self):
#         print(self.n,self.a)
# k=karthi("karthi",20)
# k.output()

#inheritance________

#5 types...................

#single______


# class bike:
#     def gear(self):
#         print("4 gear are available")
# class car(bike):
#     def type(self):
#         print("Is the classic car")
# b=car()
# b.type()
# b.gear()
# b.gear()
# b.type()


#multilevel___________

# class bank1:
#     def name(self):
#         print("My name is karthi")
# class bank2(bank1):
#     def age(self):
#         print("My age is 20")
# class bank3(bank2):
#     def balance(self):
#         print("My balance is 10000")
# b=bank3()
# b.name()
# b.age()
# b.balance()


#multiple____________-

# class travels():
#     def bus(self):
#         print(' bus travel to 5 hours')
# class travels2():
#     def train(self):
#         print(" train travel to 3 hours")
# class trip(travels,travels2):
#     def flight(self):
#         print(' flight travel to 1 hours')
# t=trip()
# t.flight()
# t.train()
# t.bus()

#hierarical______________

# class college():
#     def address1(self):
#         print('namakkal')
# class college2(college):
#     def address2(self):
#         print('rasipuram')
# class college3(college):
#     def address3(self):
#         print('salem')
# # class allcollege(college2,college3,college):
# class allcollege(college2,college3):
#     def all(self):
#         print('namakkal','rasipuram','salem')
# a=allcollege()
# a.all()
# a.address3()
# a.address2()
# a.address1()


#encapsulation_____________

# class bank:
#     value=500000
#     def customer1(self):
#         print('karthi','\n','10000','\n','salem')
#     def customer2(self):
#         print('saran','\n','20000','\n','namakkal')
# b=bank()
# b.customer1()
# b.customer2()
# print(b.value)


# class bank:
#     def __init__(self):
#         self.__value=100
#     def __sam(self):
#         # print('value',self.__value)

#         print("name:sam")
#         print("a/c:123456789")
#         print("balance:1000")
#         print("place:salem")
#         print("\n")
#     def __karthi(self):
#         print("name:karthi")
#         print("a/c:12234567")
#         print("balance:20000")
#         print("place:namakkal")
#         print("\n")
# b=bank()
# b._bank__sam()
# b._bank__karthi()
# print("value",b._bank__value)

#abstraction______________


# from abc import ABC
# class bus(ABC):
#     def volvo(self):
#         print('hello')
# class str(bus):
#     def volvo(self):
#         print('it is luxury bus')
# class sat(bus):
#     def volvo(self):
#         print('train')


# b=bus()
# b.volvo()
# c=str()
# c.volvo()
# d=sat()
# d.volvo()

