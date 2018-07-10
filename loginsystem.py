# Create a dictionary to store the username as 
# the key and the password as the value for the key
login = {}

# username and password rules
print("""
Create your login!
Rules for username and password:\n
1. At least 6 characters long.
2. At least 1 number.
3. At least one uppercase character.
""")

user = input("Enter your username: ")

while len(user) < 6:
        print("\nYour username must be at least 6 characters long!")
        user = input("Enter your username: ")

while True:
    upperCount = 0
    digitCount = 0

    for i in user:
        if i.isupper():
            upperCount += 1
        if i.isdigit():
            digitCount += 1
    if upperCount == 0 or digitCount == 0:
        print("\nYour username must have at least one uppercase and digit character!")
        user = input("Enter your username: ")
    else:
        break

######################################################################################

# get password
pas = input("Enter a password: ")


while len(pas) < 6:
        print("\nYour password must be at least 6 characters long!")
        pas = input("Enter your username: ")

while True:
    upperCount = 0
    digitCount = 0

    for i in pas:
        if i.isupper():
            upperCount += 1
        if i.isdigit():
            digitCount += 1
    if upperCount == 0 or digitCount == 0:
        print("\nYour password must have at least one uppercase and digit character!")
        pas = input("Enter your password: ")
    else:
        break

# Adds the key which is the user to the login dictionary
# and makes the password the value for the key
login[user] = pas

#Ask user if he/she wants to login
ans = input("Do you want to Login? Y or N : ")

if ans.lower() == 'y':
    u = input("Enter your username: ")
    if login[u] in login:
        p = input("Enter your password: ")
        if login[u] == p:
            print("You are successfuly logged in!")
        else:
            print("There has been an error with your password.")
else:
    exit()



