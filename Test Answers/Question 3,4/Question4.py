#Question 4
#Q4.1
import string
import random
# define list of letters , digits and chars
UpperCase = list(string.ascii_uppercase)
LowerCase = list(string.ascii_lowercase)
numbers = list(string.digits)
def passwordgenerator(length):
    while True:
        try:
            passlength = int(length)
            if passlength<9:
                print('Invalid entry: please enter a number grater than 8\n')
                length = input('Enter password length: \n')  
            else:   
                password = []
                #shuffle to append randomlly
                random.shuffle(UpperCase) 
                random.shuffle(numbers)
                random.shuffle(LowerCase)
                #Apending [40% uppercase 30% lowercase and 30% numbers ] to password 
                for i in range(round(passlength * .4)):
                    password.append(UpperCase[i])
                # append digits into password
                for i in range(round(passlength * .3)):
                    password.append(LowerCase[i])
                # append punctuatuions into password
                for i in range(round(passlength * .3)):
                    password.append(numbers[i])

                password = "".join(password)

                print(f"the password is : \t" + "".join(password))
                break 
        except:
            print('Invalid entry: please enter a number\n')
            length = input('Enter password length: \n')
            
length=input("Enter the password length\n")
passwordgenerator(length)