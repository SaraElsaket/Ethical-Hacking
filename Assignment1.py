#from math import pow
'''#Tracing
#Q1.1 What is the Output
    #z = not y if (X%2 !=0) else X #if x is even (divisable by two) z=not y(Not True =False) Else z=x
    Output: False(Not t)
# Q1.2
    #Output: <class 'list'>
    #<class 'list'>'''
#Q2.1
def getNumbersFromFunc():
    x=2
    y=3
    z=4
    return(x,y,z) #Tuple
#Q2.2
def SumFunc(num1):
    def Add(num2):
        return num1+num2
    return Add
#Q3:
#Q3.1
#Check if the given number is palindrome or not
def isPalindrome(Numb):
    rev=""
    for num in Numb:
        rev=num+rev
    print(rev)
    if rev==Numb:
        return True
    else:
        return False
#Q3.2
def NewList():
    list1=[10,20,25,30,35]
    list2=[40,45,60,75,90]
    new_list=[]
    for list in list1:
        if list %2 !=0:
            new_list.append(list)
    for j in list2:
        if j %2==0:
            new_list.append(j)
    return new_list
#Q3.3
def exponent(base,exp):
    return pow(base,exp)
#q3.4
def Mult_Table_Calc(num):
    mult_List={}
    for i in range(13):
        mult_List[f'{i} * {num}']=i*num
    return mult_List
#q3.5
def reverse_list(list):
    list_length=len(list)
    rev_list=[]
    for i in range(list_length-1,-1,-1):
        rev_list.append(list[i])
    print(rev_list)
#q3.6
def PrimeNumbers(num):
    Prime_list=[]
    isprime=True
    for i in range(2,num):
        for j in range(i-1,1,-1):
            if i % j ==0:
                isprime=False
                break
        if isprime==True:
            Prime_list.append(i)
        else:
            isprime=True
    print(Prime_list)
#Q3.7
#FizzBuzz
def FizzBuzz(num):
    #if divisable by both 5 and 3
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:      #if divisable by 3
        print("Fizz")
    elif num%5==0:      #if divisable by 5
        print("Buzz")
    else:               #if not divisable by 3 or 5
        print(num)
#Q3.8
def tuple_similarity(tupl):
    isSimilar=True
    for i in range(0,len(tupl)):
        for j in range(0,len(tupl)):
            if type(tupl[i])!=type(tupl[j]):
                isSimilar=False
                break
        if isSimilar!=True:     
            break
    return isSimilar
#Fibonacci Series (0,1,1,2,3,5,8,13,21,34)
def Fibonacci(num):
    Fibonacci_list=[0,1]
    i=num-2
    while(i):
        sum=Fibonacci_list[-1]+Fibonacci_list[-2]
        Fibonacci_list.append(sum)
        i=i-1
    print(Fibonacci_list)
#nCr (nCr=!n/(!r)*(!n-r)) #n>=r>=0
def nCr(n,r):
    nfact=1
    rfact=1
    n_rfact=1
    for i in range(1,n+1):
        nfact*=i
    for j in range(1,r+1):
        rfact*=j
    for k in range(1,n-r+1):
        n_rfact*=k
    return (nfact/(rfact*n_rfact))
#calling Functions
#testing menu
while(True):
    #option to choose from
    menu = input("\nChoose From Tasks: \n 1:isPalindrome \t 2:NewList \t 3:Exponent \t 4:Multiplication Table \n "
                +"5:reverse_list \t 6:PrimeNumbers\t 7:FizzBuzz \t 8:tuple_similarity \n" 
                +" 9:Fibonacci \t 10:Combinations \t 0:Exit \n")
    #conditions to call needed functions
    if menu == "1":
        print("You chose isPalindrome")
        num=(input("Enter a Number\n"))
        print(isPalindrome(num))
    elif menu == "2":
        print("You chose NewList\n list1=[10,20,25,30,35] \n list2=[40,45,60,75,90]")        
        print(f"New list is {NewList()}")
    elif menu == "3":
        print("You chose exponent")
        base=int(input("Enter a base\n"))
        exp=int(input("Enter a exponential\n"))
        print(exponent(base,exp))
    elif menu == "4":
        print("You chose Multiplication Table")
        num=int(input("Enter a Number\n"))
        print(str(Mult_Table_Calc(num)).replace(', ',',\n '))
    elif menu == "5":
        print("You chose reverse_list")
        print("You chose reverse_list\t the list is [1,3,7,4,5]")
        reverse_list([1,3,7,4,5])
    elif menu == "6":
        print("You chose PrimeNumbers")
        num=int(input("Enter a Number(range)\n"))
        PrimeNumbers(num)
    elif menu == "7":
        print("You chose FizzBuzz")
        num=int(input("Enter a Number\n"))
        FizzBuzz(num)
    elif menu == "8":
        print("You chose tuple_similarity")
        print("the tuple is (1,2,3,'4')")
        print(tuple_similarity((1,2,3,'4')))
        print(" second test the tuple is (1,2,3,4)")
        print(tuple_similarity((1,2,3,4)))
    elif menu == "9":
        print("You chose Fibonacci") 
        num=int(input("Enter a number of series elements\n"))
        Fibonacci(num)
    elif menu == "10":
        print("You chose Combinations") 
        objects=int(input("Enter a objects(n)\n"))
        samples=int(input("Enter a samples(r)\n"))
        print(nCr(objects,samples))
    elif menu == "0":
        print("Bye bye")
        break                               #To get out of the loop
    else:
        print("Invalid number")
