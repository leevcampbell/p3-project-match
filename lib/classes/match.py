from pulp import *
from lib.classes.users import User

# from lib.classes.sendemail import send_email




def match():

    current_user = User.grab_current_user()
    match_users = User.query_for_match()
    matched_users = []
    
    for match_user in match_users:
        if match_user.quickie == "y" or match_user.long_term == "y" or match_user.drinks == "y":
            if current_user.quickie == "y" or current_user.long_term == "y" or current_user.drinks == "y":
                print(f"You and {match_user.name} are a match!")
                matched_users.append(match_user)
            elif current_user.long_term == "y" and match_user.long_term == "y":
                print(f"You and {match_user.name} are a match!")
                matched_users.append(match_user)
            elif current_user.drinks == "y" and match_user.drinks == "y":
                print(f"You and {match_user.name} are a match!")
                matched_users.append(match_user)
    print("Your matches are:")
    for match in matched_users:
        print(match.name + " " + "❤️‍🔥")
    else:
        print("You have no matches, try again later!")
        

    
        # send_email(match.email, match.name)
            
        

#     users = ['Ben', 'Kate', 'Jack', 'Jill', 'Robert', 'Rosa']
#     preferences = {
#     ("Ben", "Kate"): 2,  # Ben wants a long-term relationship with Kate
#     ("Ben", "Jill"): 1,    # Ben wants to have drinks with Jill
#     ("Ben", "Robert"): 0,  # Ben wants to have a quickie with Robert
#     ("Ben", "Jack"): 1,  # Ben wants drinks with Jack
#     ("Ben", "Rosa"): 0, # Ben wants to have a quickie with Rosa
#     ("Kate", "Jack"): 2, # Kate wants a long-term relationship with Jack
#     ("Kate", "Robert"): 0, # Kate wants to have a quickie with Robert
#     ("Kate", "Ben"): 0, # Kate wants to have a quickie with Ben
#     ("Kate", "Rosa"): 0,   # Kate wants to have a quickie with Rosa
#     ("Kate", "Jill"): 1, #Kate wants to have drinks with Jill
#     ("Jack", "Jill"): 2, # Jack wants a long-term relationship with Jill
#     ("Jack", "Rosa"): 1,   # Jack wants to have drinks with Rosa
#     ("Jack", "Ben"): 1, #Jack wants to have drinks with Ben
#     ("Jack", "Kate"): 2, #Jack wants to have a long term relationship with Kate
#     ("Jack", "Robert"):0, #Jack wants to have a quickie with Robert
#     ("Jill", "Robert"): 2, # Jill wants a long-term relationship with Robert
#     ("Jill", "Rosa"): 1,   # Jill wants to have drinks with Rosa
#     ("Jill", "Ben"): 1, #Jill wants to have drinks with Ben
#     ("Jill", "Kate"): 1, #Jill wants to have drinks with Kate
#     ("Jill", "Jack"):2, #Jill wants to have a long term relationship with Jack
#     ("Robert", "Rosa"): 2, # Robert wants a long-term relationship with Rosa
#     ("Robert", "Ben"): 1,  # Robert wants to have drinks with Ben
#     ("Robert", "Kate"): 0, # Robert wants to have a quickie with Kate
#     ("Robert", "Jack"):0, #Robert wants to have a quickie with Jack
#     ("Robert", "Jill"): 2, #Robert wants a long-term relationship with Jill
#     ("Rosa", "Ben"): 1, #Rosa wants to have drinks with Ben
#     ("Rosa", "Kate"): 2,   #Rosa wants a long term relationship with Kate
#     ("Rosa", "Jack"): 1,   #Rosa wants to have drinks with Jack
#     ("Rosa", "Jill"): 1,   #Rosa wants to have drinks with Jill
#     ("Rosa", "Robert"): 2 # Rosa wants a long-term relationship with Robert
# }
#     vars = LpVariable.dicts("Match", (users, users), 0, 1, LpBinary)
#     prob = LpProblem("Match Making Problem", LpMaximize)
#     prob += lpSum([vars[i][j] for i in users for j in users if i != j])  #"total matches"
#     for i in users:
#         prob += lpSum([vars[i][j] for j in users if i != j]) == 1, f"User {i} can only be matched once"
#     for i in users:
#         for j in users:
#         # if i != j:
#         #     if preferences[(i, j)] == 1 or preferences[(i,j)] == 2:
#         #         prob += vars[i][j] <= vars[i][j], f"If matched, {i} should have a long-term relationship with {j}"
#         #     elif preferences[(i,j)] == 0:
#         #         prob += vars[i][j] <= vars[i][j], f"If matched, {i} should have a quickie with {j}"
#         #     else:
#         #         prob += vars[i][j] <= 1 - vars[i][j], f"If matched, {i} should go for drinks with {j}"
#             if i != j:
#                 if preferences[(i, j)] == 1 or preferences[(i, j)] == 0 or preferences[(i, j)] == 2:
#                     prob += vars[i][j] <= vars[i][j], f"If matched, {i} should have a quickie with {j}"
#                     prob += vars[i][j] <= vars[i][j], f"If matched, {i} should go for drinks with {j}"
#                     prob += vars[i][j] <= vars[i][j], f"If matched, {i} should have a long-term relationship with {j}"
#     prob.solve()
#     matches={}
#     for i in users:
#         for j in users:
#             if i != j and vars[i][j].value() == 1:
#                 print(f"{i} is matched with {j}")
#     for user, match in matches.items():
#         send_email(user, match)

