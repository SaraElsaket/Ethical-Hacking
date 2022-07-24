import os
while True:
    try:
        command = input('\\ ')
        if command.lower() == 'exit': #for avoiding not recognized it if capitalized
            print('See you later ')
            break
        res = os.system(command) # os system command to run cmd
    except:
        command = input('\\ ')