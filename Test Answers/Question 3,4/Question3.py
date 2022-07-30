#Question 3
#3.1
from math import pi
def vowelCounter(word):
    while(True):
        try:
            if word.isalpha():
                count=0
                vowel=["a","i","o","u","e"]
                for i in word:
                    if i in vowel: #youloop 
                        count+=1
                return count
            raise TypeError
        except TypeError:   #error Raised when a function or operation is applied to an object of an incorrect type
            print("invalid entry\n")
            word = input('Enter a string\n')
#Q3.2
def sum_numbers(num):
    while(True):
        try:
            num=int(num)
            if num ==0:
                return 0
            else:   
                return num+sum_numbers(num-1)
        except:
            print("invalid entry\n")
            num = input('Enter a Number\n')
#Q3.3
def Fibonacci(num):
    #base start numbers
    Fibonacci_list=[0,1]
    i=num-2
    while(i):
        #-1 is last item in list -2 the item before last item
        sum=Fibonacci_list[-1]+Fibonacci_list[-2] 
        Fibonacci_list.append(sum)
        i=i-1
    print(Fibonacci_list)
# Fibonacci(10)
#q3.4
def searchindict(dict,num):
    exist=False
    for i in dict.values():
        if i==num:
            exist=True
    return exist
#q3.5
class Circle:
# (-> None,str,int)*specialized comments with a defined syntax. it doesnot make an error if return differs(except if it predefined function)
    def __init__(self,radius=1.0,color="red") -> None: 
        self.radius=radius
        self.color=color
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
class Cylinder(Circle):
    def __init__(self,radius,color,height=1.0) -> None:
        super().__init__(radius,color)
        self.height=height
    #setters
        def setheight(self,height):
            self.height=height
    #getters    
    def getheight(self):
        return self.height
    #cylinder volume = Height*pi*R^2
    def GetVolume(self):
        return round(self.height*pow(self.radius,2)*pi,2)

#calling Functions
#testing menu
while(True):
    #option to choose from
    menu = input("\nChoose From Tasks: \n 1:vowelCounter \t 2:sum_numbers \t 3:Fibonacci" 
    +"\t 4:does the number exist in dictionary\t 5:Volume of cylinder \t0:Exit \n")
    #conditions to call needed functions
    if menu == "1":
        print("You chose vowelCounter")
        word=input('Enter a string\n')
        print(f"the nummber of vowels in the word are:{vowelCounter(word)}")
    elif menu == "2":
        print("You chose sum from zero to the number you enter")        
        num = input('Enter a Number\n')
        print(f"The sum from zero to entered number is:{sum_numbers(num)}")
    elif menu == "3":
        print("You chose Fibonacci series(till 34)")
        Fibonacci(10)
    elif menu == "4":
        print("You chose if 200 exist in the dictionary")
        dict={'a': 100, 'b': 200, 'c': 300}
        print(f"dict is :{dict}")
        print(searchindict(dict,200))
    elif menu == "5":
        print("get cylinder volume")
        try:
            height = input('Enter its height\n')
            radius = input('Enter it radius\n')
            cyl=Cylinder(int(height),None,int(radius))
            print(cyl.GetVolume())
        except:
            print("invalid entry:please enter numbers only")
    elif menu == "0":
        print("Bye bye")
        break                               #To get out of the loop
    else:
        print("Invalid number")