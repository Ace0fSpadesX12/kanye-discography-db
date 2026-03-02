def security_login(name , password):
    logging_in = True
    while logging_in: 
        login_attempts_remaining = 3
        if name == "Sean" and password == "Ace":
            print("You are authorized to continue.")
            input("Please press Enter, Sean.")
            print(f"Hello, {name}, welcome to the crushing world of Python Dev!")
            logging_in = False
        else:
            print("You do not have access. Please try again!")   
            name = input("Please re-enter your name: ")
            password = input ("Please re-enter your password: ")
            login_attempts_remaining -= 1
            if login_attempts_remaining == 0:
                break
            
            

security_login("Seahorn","Ace")
