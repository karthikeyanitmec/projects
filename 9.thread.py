#single thread____

from threading import *

class boys(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm

    def run (self):
        print('welcome to our home',self.name)
class girls(Thread):
    def __init__(self,gf):
        super().__init__()
        self.gname=gf
    def run (self):
        print("why are you coming",self.gname)

o=boys("karthi")
o1=girls("shruthi")
o.start()
o1.start()


#multithread____





