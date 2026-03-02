#This Program Will Determine What Year You Can Drink Legally!
#1996-2017

LEGAL_DRINKING_AGE = 21
current_year = 2026
#your_currentage_now = input("Please input your current age to determine what year you are/were legal to drink ")
#your_legal_year = (LEGAL_DRINKING_AGE - int(your_currentage_now) + current_year)


#if your_legal_year > 2026:
    #print(f"You will be able to legally drink in the year {your_legal_year}!!")

#elif your_legal_year == 2026:
    #print("You will be able to drink legally this year!! Cheers!!")

#else:
# print(f"You've been able to legally drink 🍻 since the year {your_legal_year}!!")


def when_can_i_drink(age, name):
    LEGAL_DRINKING_AGE = 21
    current_year = 2026
    your_legal_year = (LEGAL_DRINKING_AGE - int(age) + current_year)
    if your_legal_year > 2026:
        print(f"You are currntly {age} and will be able to legally drink 🍻 in the year {your_legal_year}, {name}!!")

    elif your_legal_year == 2026:
        print(f"You are currently or about to be {age} and will be able to drink 🍻 legally this year {name}!! Cheers!!")

    else:
        print(f"You are currently {age} and have been able to legally drink 🍻 since the year {your_legal_year}, {name}!!")




when_can_i_drink(25,"Sean")