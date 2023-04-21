from lib.classes.users import User
from lib.classes.showbanner import show_banner
from lib.classes.match import match


show_banner()

def main_menu():

    print("1. Create your profile")
    print("2. View all users")
    print("3. Let\'s DRnQ")
    print("4. Exit")
    user_input = input(">>> ")
    if user_input == "1":
        name = input("Name: ") 
        email = input("Email: ")
        quickie = input("Quickie? (y/n): ")
        longrel = input("Long-term Relationship? (y/n): ")
        drinks = input("Just Drinks? (y/n): ")
        profile = User(name , email , quickie , longrel , drinks )
        User.create(profile)
        print("\n")
        print(profile)
        print("\n")
        print("Your profile has been created! Now let's DRnQ!💞🍸")
        print("\n")
        sub_menu()
    elif user_input == "2":
        User.query_all()
        print("\n")
        main_menu()
    elif user_input == "3":
        match()
    elif user_input == "4":
        while True:
            user_input = input("Are you sure you want to exit? (y/n) ")
            if user_input == "y":
                print("🖕🍸")
                break
    else:
        print("Invalid input")
            



def sub_menu():
    print("1. View All Users")
    print("2. Let\'s DRnQ!🍸")
    print("3. Exit")
    user_input = input(">>> ")
    if user_input == "1":
        User.query_all()
        sub_menu()
    if user_input == "2":
        match()
        main_menu()
    if user_input == "3":
        exit()
