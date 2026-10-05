password = input("enter the password")
if len(password)>= 8 and any(char in "!@#$%&*" for char in password):
    print("vallide password")
else:
    print("invalide password")    