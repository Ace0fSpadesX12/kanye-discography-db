import time 
import sys
PASSWORD = "best" 
system_cal = {"System connecting..", 
"System connecting...", 
"System connecting...."} 

print("Welcome to Banking with \"Trust\"") 

def end_system_protocol(): 
    print("We're sorry, you've run out of attempts. Please try again later") 
    sys.exit()    

def user_name_authentification():
    user_name = input("Please enter your username here - ")
    user_attempts = 3
    while True:
        if user_name == "Sean":
            break
        else:
            user_attempts -= 1
            if user_attempts == 0:
                end_system_protocol()
            if user_attempts == 1:
                print("Warning. One username attempt left before lockdown.")
        user_name = input("Please try again. Enter your username here - ")                

def passwd_authentification():
    user_check = False 
    password_attempts = 3 
    fail_check = False 
    while True: 
        user_check = input("Please enter your password... ") 
        if user_check == PASSWORD: 
            break
        else: 
            print("Access denied") 
        password_attempts -= 1 
        if password_attempts == 1: 
            print("Warning. One attempt remaining before safety lockout.") 
        if password_attempts == 0: 
            fail_check = True 
            return fail_check 


user_name_authentification()
fail_check = passwd_authentification()

if fail_check: 
    end_system_protocol() 
else: 
    for check in system_cal: 
        print(check) 
        time.sleep(1.5) 
    print("Log in successful!!")