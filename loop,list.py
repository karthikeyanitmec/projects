#atm task 2 debit and withdraw4_________________________________________________________________________

#ass/ingnment operator

# account={
#     "number":12345567,
#     "holder":"karthi",
#     "balance":45000
# }

# userin=int(input("tell is your money"))
# account['balance']+=userin
# print(userin,"is deposited",account["balance"])


# count=int(input("how many tickets"))
# payable=count*500
# print(count,"added tickets",payable)

# alpha=140
# beta=240
# print(alpha,beta)
# print(alpha&240)
# print(beta|140)


# print(100&250)
#logical and relational


# skill=input("tell ur proficiency")
# project=int(input("how many project is done"))
# print("associate engineer",(skill=='java' or skill=="python" and project>2))
# print("devops engineer",(skill=='c++' or skill=='agile' or skill=='java'))
# print("developer engineer",(project>=5 and (skill=='javascript' or skill=='python' or skill=='java')))


#odd
# value1=int(input("enter"))
#value2=int(input("enter the 2 number"))
# calculate=value1%2==0
# print("it is even",calculate)
# calculate2=value1%2!=0
# print("it is odd",calculate2)
# print(" even number",value1%2==0)


# a=int(input("enter the number1:"))
# b=int(input("enter the number2:"))
# add=a+b
# sub=a-b
# div=a/b
# mul=a*b
# if()



#task 2 wonderla concept 3 category______________________________________________________________________


# age=int(input("enter your age"))
# if(age>=18):
#     print("welcome to wonderla games")
#     gender=input("enter your gender")
#     if (gender=="male" or gender=="female"):
#         print("eligible for action games")
#     else:
#         print("sry,ur not eligible for action games")
# else:
#     print("sry,ur not eligible for wonderla")


# ward=int(input("enter your ward number"))
# if (ward>0 and ward<=10):
#     boothno=int(input("enter your booth number"))
#     if (boothno<=10):
#      print("your booth hall")
#     elif(boothno==50):
#      print("your booth hall is 1")
#     else:
#       print("booth hall is not available")
# else:
#   print("your wardnumber is not")
    

# seat=1
# while seat<=10:
#     amount=int(input("enter your amt"))
#     if (amount<=100):
#      print("your seat no is :",seat)
#      seat+=1
#     else:
#      print("insufficient amt")


# seat=1
# while seat<=30:
#     if seat%5!=0 and seat%2!=0:
#        amount=int(input("enter your amt"))
#        if (amount<=100):
#            print("your seat no is :",seat)
#            seat +=1
#        else:
#            print("insufficient amt")
#     else:
#         seat +=1
#         continue

# hire =5
# while hire>0:
#     skill=input("tell us your skill")
#     project=int(input("tell us your project"))
#     if (skill=='java' or skill =='python') and project>5:
#         print("you are hired")
#         hire -=1
#     else:
#         print("you are not hired")


# #for loop


# for point in "karthi":
#     print(point)



# alpha={123,"keyan",1223,12.4}
# for i in alpha:
#     print(i)

# for i in range (0,5):
#     print(i)


# tup=("karthi",20,"tcs",5.5)
# for p in tup:
#     print(p)


# pos=1
# while pos<len(tup):
#     print(tup[pos])
#     pos+=1
 

# for i in range(len(tup)):
#     print (tup[i])


# for i in range(len(tup)-1):
#     print (tup[i])


# for i in range(len(tup)-2):
#     print (tup[i])

# for i in range(len(tup)-1,-1,-1):
#     print (tup[i])

# stock = 10
# for stock in range (0,5):
#     amt=int(input("enter your amt"))
#     if amt>=1000:
#         print("stock is purchased")
#         stock-=1
#     else:
#         print("insufficient")

# for i in range(5):
#     print("*")
#     print("* /n "*")

# prop=["karthi",10,5.5,'k']
# print(len(prop))


# print(prop)
# prop.append("engineer")
# print(len(prop))
# print(prop)


# prop.insert(1,"10.56")
# print(prop)
   

# amt=[1000,3445,24578,3456,234,223]
# print(min(amt))


# print(amt[1,2])___________________________tsk_________
# print(max(amt))

# print(sum(amt))

# print(amt.pop())

# print(amt.pop(1))


# print(amt.reverse())
# print(amt)


# print(amt)
# print(amt.reverse())
# print(amt)


# list=[1,2,3,4,5,6,6,6]
# print(len(list))


# li=list.count(2)
# print(li)

# # a=list.copy()
# # print(a)

# a=[1,2,3,4,5,5,67,89]
# print("originl state",a)