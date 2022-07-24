# 1-Overall Apericiation app
def Gradingsystem(num):
    if num>=85 and num<=100:
        print(str(num)+ "\tEquivalet to\t" +"Grade:Excellent")
    elif num>=75 and num<85:
        print(str(num)+ "\tEquivalet to\t" +"Grade:Very Good")
    elif num>=65 and num<75:
        print(str(num)+ "\tEquivalet to\t" +"Grade:Good")
    elif num>=50 and num<65:
        print(str(num)+ "\tEquivalet to\t" +"Grade:Pass")
    elif num<50 and num>=0:
        print(str(num)+ "\tEquivalet to\t" +"Grade:Fail")
    else:
        print("Invalid number")
# 2- FizzBuzz
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
# 3- even or odd
def even_or_odd(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")
#4- Check if String is palindrome or not(the word reversed Equal the Original word )
def Palindrome(word):
    word_length=len(word)
    rev=""
    for letter in range(-1,-(word_length+1),-1): # loop in reversed order
        rev+= word[letter]                       #Reverese the Entered word
    if rev.lower()==word.lower():           #To avoid if the word begins with a capital letter
        print(word +" is Palindrome")
    else:
        print(word +" is not Palindrome")
#Another Method
'''#def Palindrome(word):
    rev=""
    for letter in word:                      # i is characters of the entered word 
        rev = letter + rev                   #added it to rev(reversed)
    if rev.lower()==word.lower():       #to avoid is word begins with a capital letter
        print(word +" is Palindrome")
    else:
        print(word +" is not Palindrome")'''
#5- Calculate rectangele area and Perimeter
#Rectangle Rules:    Area=Length * Width     Perimeter=2*length +2*Width  
def rectangle(l,w):
    Area=l*w
    perimeter=2*l+2*w
    print("Rect_Area:"+str(Area) +"\t"+"Rect_perimeter:"+str(perimeter))
#testing menu
while(True):
    #option to choose from
    menu = input("\nChoose From Tasks: \n 1:Gradding System \n 2:FizzBuzz \n"
                +" 3:Even or Odd \n 4:Palindrome or not \n 5:Rectangle \n 6:to split the sentence \n 0:Exit\n")
    #conditions to call needed functions
    if menu == "1":
        print("You chose Gradding System")
        num=int(input("Enter your grade\n"))
        Gradingsystem(num)
    elif menu == "2":
        print("You chose FizzBuzz")
        num=int(input("Enter a Number\n"))
        FizzBuzz(num)
    elif menu == "3":
        print("You chose Even or Odd")
        num=int(input("Enter a Number\n"))
        even_or_odd(num)
    elif menu == "4":
        print("You chose Palindrome or not")
        input_word=input("Enter a word\n")
        Palindrome(input_word)
    elif menu == "5":
        print("You chose Rectangle")
        len=int(input("Enter length\n"))
        width=int(input("Enter Width\n"))
        rectangle(len,width)
    elif menu =="6":
        print("you chose split a sentence")
        input_sentence = input("Enter a sentence\n")
        # Printing the words of a sentence
        for word in input_sentence.split():  # it splits the sentence at any spaces
            print(word)
    elif menu == "0":
        print("Bye bye")
        break                       #To get out of the loop
    else:
        print("Invalid number")
