amount=int(input("enter the withdrawal amount"))
balance=int(input("enter the balance amount"))
if amount <= balance and amount % 500 == 0:
    print("transactions is allowed")
else:
    print("transactions is not allowed")    
