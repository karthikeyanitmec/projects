#tuple_______________

# a=("karthi",2,0,0,3)
# a=["karthi",2,0,0,3]

# print(a)
# print(type(a))
# print(a[0:4])
# print(a[:3])

# a=('karthi','saran','joo','sri',123)
# b=list(a)
# b.append('vasanth')
# a=tuple(b)
# print(a)

# b=("vasanth",)
# a+=b
# print(a)


# a=('karthi','saran','joo','sri',123)
# a=a*2
# print(a)

# b=(4,5,6,8,7)
# c=a+b
# print(c)

# a=('karthi','saran','joo','sri',123)
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1

# b=list(a)
# b.remove("saran")
# a=tuple(b)
# print(a)

# a={"karthi","saran","joo","karthi"}
# print(a)

# s=set(("karthi","saran","joo","karthi"))
# print(s)

# s.update("vasanth")
# print(s)

# a=["vasanth"]
# s.update(a)
# print(s)

# # k=s.pop()
# for i in s:
#     print(i)

# print(k)

# print("joo" in s)


#dictionary_______________


# a={"name":"karthi","age":20,"address":"namakkal"}
# print(a)
# a['number']=1234556787
# print(a)
# a.update({"pin code":423253})
# print(a)

# details={"name":"karthi","age":20,"address":"namakkal"}
# # print(details)
# # details.clear()
# # print(details)
# k=details.copy()
# print(k)
# a=k.get("age")
# print(a)
# a=k.get("bio","number")
# print(a)

# g=k.keys()
# print(g)


# g=k.values()
# print(g)


# g=k.items()
# print(g)


# details={"name":"karthi","age":20,"address":"namakkal"}
# k=details.setdefault("frds","kavi")
# # print(k)

# details.update({"car":"audi"})
# print(details)

# for i in details:
#     print(i)
# for h in details.values():
#     print(h)

# for i,j in details.items():
#     print(i,j)


# details.pop("age")
# print(details)


# del details["name"]
# print(details)


# if 'name' in details:
#     print("execute")


# details={"name":"karthi","age":20,"address":"namakkal"}
# a=details
# print(a)

# del a["age"]
# print(a)


# def funct():
#     ans=input("tell us your destination:")
#     if (ans=="chennai"):
#         print("dangerous")
#     elif(ans=="salem"):
#         print("safe")
#     elif(ans=="bangalore"):
#         print("very dangerous")
#     else:
#         print("enter your valid city")
#use defined__________________

# def function():
#     ans=input("tell us your destination:")
#     if (ans=="chennai"):
#         print("dangerous")
#     elif(ans=="salem"):
#         print("safe")
#     elif(ans=="bangalore"):
#         print("very very dangerous")
#     else:
#         print("enter your valid city")
# function()

#pre defined______________

# def job(qual,ref):
#     if qual=="ug" and ref=="hr":
#         print("get offer letter")
#     elif qual=="pg" and ref=='tl':
#         print("rejected")
#     else:
#         print("waiting list")
# job('student','learn')
# job('pg','tl')
# job(qual='ug',ref='hr')
# def ask(purpose):
#     if purpose=="economy":
#         print("ok")
#     elif purpose=="social":
#         print("double kk")
#     else:
#         print("nothing")
# ask("economy")


# def register(name,location,prefix="mr/miss,mrs"):
#     if location=='salem':
#         print(prefix,name,"has approved in ",location)
#     elif location == "chennai":
#         print(prefix,name,"waiting state in ",location)
#     else:
#         print("not eligible")
# register("zealous",'chennai')
# register('karthi','salem','mr')
# register('has been completed','sss')



balance=[200000,10000,1000,10]

def debit(money=0,pos=0):
    if money<=balance[pos]:
        balance[pos]-=money
        print(money,"debited")
        return balance[pos]
    else:
        print("can't debit")
h=debit(1000,1)
print(h)
j=debit(10,3)
print(j)







