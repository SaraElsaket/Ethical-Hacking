#imports
from math import ceil, floor, pi
#1.1
class Circle:
# (-> None,str,int)*specialized comments with a defined syntax. it doesnot make an error if return differs(except if it predefined function)
    def __init__(self,radius,color) -> None: 
        self.radius=radius
        self.color="red"
#setters
    def setradius(self,radius):
        self.radius=radius
    def setcolor(self,color):
        self.color=color
#getters    
    def getradius(self):
        return self.radius
    def getcolor(self):
        return self.color
    def getArea(self):
        return round(self.radius*self.radius*pi,2)
    def __str__(self):
        return f"radius:{self.radius} \n color:{self.color}"
#1.3
class Rectangle:
    #constructor
    def __init__(self,length,width):
        self.length=length
        self.width=width
    #setters
    def setlength(self,length):
        self.length=length
    def setwidth(self,width):
        self.width=width 
    #getters
    def getlength(self):
        return self.length
    def getwidth(self):
        return self.width
    def getArea(self):
        return round(self.length*self.width,2)
    def getperimeter(self):
        return round(2*(self.length+self.width),2)
    def __str__(self) -> str:
        return f"length:{self.length} \n width:{self.width}"
#1.4
class Employee:
    def __init__(self,id,firstName,lastName,salary) -> None:
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
    #setters
    def setsalary(self,salary):
        self.salary=salary
    #getters
    def getID(self):
        return self.id
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getName(self):
        return self.firstName+self.lastName
    def getSalary(self):
        return self.salary
    def getAnnualSalary(self):
        return round(self.salary*12)
    def raiseSalary(self,percent):
        increase=self.salary*(percent/100)
        newSalary=self.salary+increase
        self.salary=floor(newSalary) #to match the website test case
        return self.salary
    def __str__(self) -> str:
        return f"Employee[id={self.id},name={self.firstName + self.lastName},salary={self.salary}]"
#1.6
class Account:
#making default value for balance to allow calling function without it
    def __init__(self,id,name=None,balance=0) -> None: 
        self.id=id
        self.name=name     
        self.balance=balance

    #getters
    def getID(self):
        return self.id
    def getName(self):
        return self.name
    def getBalance(self):
        return self.balance
    def credit(self,amount):
        self.balance+=amount
        return self.balance
    def debit(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("amount exceeded balance")
        return self.balance
    def transferto(self,account,amount):
        if self.balance>=amount:
            self.balance-=amount
            account.balance+=amount
        else:
            print("amount exceeded balance")
        return self.balance
    def __str__(self) -> str:
        return F"Account[id={self.id},name={self.name},balance={self.balance}]"
#test functions
def circletest():
    circle1=Circle(5,"blue")
    print(circle1)
    circle1.setradius(2)
    circle1.setcolor("black")
    print(f"radius:{circle1.getradius()} \t color:{circle1.getcolor()}")
    print(f"getArea:{circle1.getArea()}")
    print(f"tostring:{circle1.__str__()}")
def rectangletest():
    rectangle=Rectangle(1.2,3.4)
    print(rectangle)
    rectangle.setlength(5.6)
    rectangle.setwidth(7.8)
    print(f"length:{rectangle.getlength()} \t width:{rectangle.getwidth()}")
    print(f"getArea:{rectangle.getArea()}")
    print(f"getperimeter:{rectangle.getperimeter()}")
def Employeetest():
    employee=Employee(3,"Peter","Tan",2500)
    print(employee)
    employee.setsalary(999)
    print(f"Employee[id={employee.getID()}\n firstname={employee.getFirstName()} \n lastname:{employee.getLastName()} \n salary={employee.getSalary()}]")
    print(f"Annual salary:{employee.getAnnualSalary()}")
    print(f"salary after raise by 10%:{employee.raiseSalary(10)}")
    print(employee)
def Accounttest():
    account=Account("A101", "Tan Ah Teck", 88)
    account2=Account("A102", "Kumar")
    print(account)
    print(f"Employee[id={account.getID()}\n firstname={account.getName()}\n Balance={account.getBalance()}]")
    account.credit(100)
    print(account.__str__())
    account.debit(50)
    print(account.__str__())
    account.debit(500)
    print(account.__str__())
    account.transferto(account2,100)
    print(f"after transfer:{account.__str__()}")
    print(f"after transfer:{account2.__str__()}")
    #extratest
    account3=Account("A103")
    print(account3.__str__())
    print(account3.getName())

#menu for testing
while(True):
    #option to choose from
    menu = input("\nChoose From testing cases for clases: \n 1:Circle \n 2:Rectangle \n"
                +" 3:Employee \n 4:Account \n 0:Exit\n")
    #conditions to call needed functions
    if menu == "1":
        print("You chose Circle test")
        circletest()
    elif menu == "2":
        print("You chose rectangle test")
        rectangletest() 
    elif menu == "3":
        print("You chose Employee test")
        Employeetest()
    elif menu == "4":
        print("You chose Account test")
        Accounttest()
    elif menu == "0":
        print("Bye bye")
        break                       #To get out of the loop
    else:
        print("Invalid number")