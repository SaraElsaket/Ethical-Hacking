#Another method for password generator 
#Imports

from tkinter import *
import string 
import random

#variables decleration
global passLen
global charlen
global Special_charlen
global  numlen
global generatedpass
#passeword parts constants
letters = list(string.ascii_letters)
digits = list(string.digits)
chars = list(string.punctuation)

#for invalid entries
#for entering password length  < 8
def invalidentry():
    global Invaild_Entry
    Invaild_Entry = Toplevel(window)
    Invaild_Entry.title("invalid entry")
    Invaild_Entry.geometry("150x100")
    Label(Invaild_Entry, text="Invalid Password length").pack()
    Button(Invaild_Entry, text="OK", command=delete_Invaild_Entry).pack()
#for not entering a number
def invalidentry2():
    global Invaild_Entry
    Invaild_Entry = Toplevel(window)
    Invaild_Entry.title("invalid entry")
    Invaild_Entry.geometry("150x100")
    Label(Invaild_Entry, text="must enter a number").pack()
    Button(Invaild_Entry, text="OK", command=delete_Invaild_Entry).pack()
# for destroying the alert(message)
def delete_Invaild_Entry():
    Invaild_Entry.destroy()
#password generator function
def passwordgenerator():
#variable decleration
    password = []

    #Shuffle for elements of password
    random.shuffle(letters)
    random.shuffle(digits)
    random.shuffle(chars)
    try:
        if passLen.get() < 8 : 
            invalidentry()
    except:
        invalidentry2() 
    # append letters into password
    for i in range(charlen.get()):
        password.append(letters[i])
    # append digits into password
    for i in range(numlen.get()):
        password.append(digits[i])
    # append punctuatuions into password
    for i in range(Special_charlen.get()):
        password.append(chars[i])

    password = "".join(password[0:])
    output.set(f"Your password is : \n  {password}")

# Main Window(GUI)
window = Tk(className="Login")   #blank window
window_title = Label(window, text="Python GUI") # name The GUI window
window.geometry('600x250') #window geometry
window_title.pack() #this is assigning any space it finds to the Title
#GUI variables
passLen = IntVar()
charlen = IntVar()
Special_charlen = IntVar()
numlen = IntVar()
output = StringVar()
#take password entries from user
Label(window, text='password length').pack()
ent1 = Entry(window, textvariable=passLen).pack()
Label(window, text='character length').pack()
ent2 = Entry(window, textvariable=charlen).pack()
Label(window, text='Special character length').pack()
ent3 = Entry(window, textvariable=Special_charlen).pack()
Label(window, text='numbers length').pack()
ent4 = Entry(window, textvariable=numlen).pack()
btn =Button(window,text="pass generator",activebackground='red',command=passwordgenerator) 
btn.pack() 
outputLabel = Label(window, textvariable = output).pack()
window.mainloop()  # it make window run untill the exit button is clicked

