# # del details["name"]
# # print(details)



# # if 'name' in details:
# #     print("execute")


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
# # #use defined__________________

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

# # #pre defined______________

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



# balance=[200000,10000,1000,10]

# def debit(money=0,pos=0):
#     if money<=balance[pos]:
#         balance[pos]-=money
#         print(money,"debited")
#         return balance[pos]
#     else:
#         print("can't debit")
# h=debit(1000,1)
# print(h)
# j=debit(10,3)
# print(j)

#recursive______


# def rec(k):
#     if (k>0):
#         result = k+rec(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# rec(4)
