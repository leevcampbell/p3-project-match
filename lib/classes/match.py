from pulp import *
from lib.classes.users import User
from lib.classes.sendemail import send_email



def match():

    # this function will match users based on their attributes but only if they have at least 2 attributes in common

    current_user = User.grab_current_user()
    match_users = User.query_for_match()
    matched_users = []
    
    for match_user in match_users:
        if match_user.id == current_user.id:
            continue
        num_attributes_match = 0
        if match_user.quickie == "y":
            num_attributes_match += 1
        if match_user.long_term == "y":
            num_attributes_match += 1
        if match_user.drinks == "y":
            num_attributes_match += 1
        if num_attributes_match >= 2:
            if current_user.quickie == "y":
                num_attributes_match += 1
            if current_user.long_term == "y":
                num_attributes_match += 1
            if current_user.drinks == "y":
                num_attributes_match += 1

        if num_attributes_match >= 2:
            print(f"You and {match_user.name} are a match!❤️🍸")
            matched_users.append(match_user)
            send_email('pythontestingphase3@gmail.com', "ekzewlnqqveldcri", match_user, current_user)
            
    if not matched_users:
        print("No matches found. Try again later.")

