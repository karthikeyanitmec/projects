class book:

    def __init__(self,bookid=0,bookname="",bookprice=0):
        self.__bookid=bookid
        self.__bookname=bookname
        self.__bookprice=bookprice
    def set_bookid(self,bookid):
        self.__bookid=bookid
    def set_bookname(self,bookname):
        self.__bookname=bookname
    def set_bookprice(self,bookprice):
        self.__bookprice=bookprice

    def get_bookid(self):
        return self.__bookid
    def get_bookname(self):
        return self.__bookname
    def get_bookprice(self):
        return self.__bookprice
    
    def __str__(self):
        return str(self.__bookid)+""+self.__bookname+""+str(self.__bookprice)
    
##get inputs__

books=[]
n=int(input('enter the total no of books:'))

for i in range(n):
    bookid=int(input('enter your bookid:'))
    bookname=input('enter your book name:')
    bookprice=int(input('enter your book price:'))
    print()
    show=book(bookid,bookname,bookprice)
    books.append(show)

##display

for show in books:
    print('bookid:',show.get_bookid())
    print('bookname',show.get_bookname())
    print('bookprice',show.get_bookprice())
    print()

##search___

bookid=int(input('enter your search bookid:'))

for show in books:
    if show.get_bookid()==bookid:
        print(show)
        break

else:print('no books available')


##delete___

bookid=int(input("enter your delete bookname:"))

for show in books:
    if show.get_bookid()==bookid:
        books.remove(show)
        print('successfully deleted')
        break

##update_ the price____________

bookid=int(input("enter your update bookid:"))
for show in books:
    if show.get_bookid()==bookid:
        new_price=int(input('enter youir new price:'))
        show.set_bookprice(new_price)
        print('update successfully')
        break
else:print('not allowed for update process')

print('bookid:',show.get_bookid())
print('bookname',show.get_bookname())
print('bookprice',show.get_bookprice())