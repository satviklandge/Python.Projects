Balance = 100000

amount = int(input("Enter the amount to withdraw: "))

if amount <= Balance :
    Balance -= amount
    print ("Withdraw successful !!")
    print ("Remaining Balance: ", Balance)

else :
    print ("Insufficient Balance !!")

