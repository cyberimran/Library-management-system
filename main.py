
listofbook0=["Python","Kahani","Akbar","Pycics","Html expert book"]  
lendofbook=[]
lendofbook1=[]
lendofbook2=[]
class Library:
    def __init__(self,name,listofbook):
        self.name=name
        self.listofbook=listofbook
    def displaybooks(self):
        print(self.listofbook)
    def addbook(self):
        add1=input("Enter book name: ")
        add2=input("Enter your user name: ")
        self.listofbook.append(add1)
        print(f"\nThanks for visit {self.name}")
    def lendbook(self):
        lend1=input("Enter book name: ")
        if lend1 in lendofbook2:
            print("This book is already lend.")
        elif lend1 in listofbook0:
            lend2=input("Enter your user name: ")
            print(f"\nThanks for visit {self.name}")
            lendofbook.append(lend2)
            lendofbook1.append(f"{lend1}: {lend2}")
            lendofbook2.append(lend1)
        else:
            print("This book is not avilable in library.")
    def returnbook(self):
            rbook1=input("Enter your book name: ")
            rbook2=input("Enter your user name: ")
            if rbook1 in lendofbook2:
                if rbook2 in lendofbook:
                    lendofbook2.remove(rbook1)
                    lendofbook.remove(rbook2)
                    lendofbook1.remove(f"{rbook1}: {rbook2}")
                    print(f"\nThanks for visit {self.name}")
                else:
                    print("Wrong input")
            else:
                print("Wrong input")

          
library=Library("Imran Library",listofbook0)  

     
while 0==0:
    i1=int(input("\n1.Display book.\n2.Add book.\n3.Lend book.\n4.Return book.\n\nEnter your choice: ")) 
    if i1==1:
        library.displaybooks()
    elif i1==2:
        library.addbook()
    elif i1==3:
        library.lendbook() 
    elif i1==4:
        library.returnbook()
    elif i1==302037:
        print(lendofbook)
        print(lendofbook2)
        print(lendofbook1)
    else:
       print("Wrong input")