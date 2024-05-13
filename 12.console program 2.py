class market:

    def __init__(self,productid=0,productname="",productprice=0,productquantity=0,productvalid_date=0,productrating=0):
        self.__id=productid
        self.__name=productname
        self.__price=productprice
        self.__quantity=productquantity
        self.__date=productvalid_date
        self.__rating=productrating

    def set_productid(self,productid):
        self.__id=productid
    def set_productname(self,productname):
        self.__name=productname
    def set_productprice(self,productprice):
        self.__price=productprice
    def set_productquantity(self,productquantity):
        self.__quantity=productquantity
    def set_productvalid_date(self,productvalid_date):
        self.__date=productvalid_date
    def set_productrating(self,productrating):
        self.__rating=productrating
    

    def get_productid(self):
        return self.__id
    def get_productname(self):
        return self.__name
    def get_productprice(self):
        return self.__price
    def get_productquantity(self):
        return self.__quantity
    def get_productvalid_date(self):
        return self.__date
    def  get_productrating(self):
        return self.__rating
       
    def __str__(self):
        return str(self.__id)+""+self.__name+""+str(self.__price)+""+str(self.__quantity)+""+str(self.__date)+""+str(self.__rating)
    
#get a user input__

store=[]
c=int(input('how many products are you buy:'))

for i in range(c):
    productid=int(input("Enter your product id:"))
    productname=input("Enter your product name:")
    productprice=int(input("Enter your product price"))
    productquantity=int(input("Enter your product quantity:"))
    productvalid_date=int(input("Enter your product valid date:"))
    productrating=int(input("Enter your product rating:"))
    print()

    products=market(productid,productname,productprice,productquantity,productvalid_date,productrating)
    store.append(products)


#dispaly the products___
for  products in store:
    print("productid:",productid)
    print("productname:",productname)
    print("productprice:",productprice)
    print("productquantity:",productquantity)
    print("productvalid_date:",productvalid_date)
    print("productrating:",productrating)

    print()

#search products__
productpricelist=int(input("How much your budget in buy a product:"))
for products in store:
    if products.get_productprice()<=productpricelist:
        print("productid:",productid)
        print("productname:",productname)
        print("productprice:",productprice)
        print("productquantity:",productquantity)
        print("productvalid_date:",productvalid_date)
        print("productrating:",productrating)
        print()



##delete___

productid=int(input("enter your delete productid:"))

for products in store:
    if products.get_productid()==productid:
        store.remove(products)
        print('successfully deleted')
        break


##update_ the price____________

productid=int(input("Enter your update productid:"))
for products in store:
    if products.get_productid()==productid:
        new_price=int(input('enter youir new price:'))
        products.set_productprice(new_price)
        break
else:print("Didn't process in update price")


print("productid:",productid)
print("productname:",productname)
print("productprice:",productprice)
print("productquantity:",productquantity)
print("productvalid_date:",productvalid_date)
print("productrating:",productrating)
print()