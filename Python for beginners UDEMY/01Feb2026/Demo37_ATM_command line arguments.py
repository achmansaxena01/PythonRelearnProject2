import sys
accBalance = 10000
lst = sys.argv

# Check if at least one argument is provided

if len(sys.argv) < 2:
    print("Usage: python atm.py <operation> [amount]")
    print("Operations: 1=Check Balance, 2=Withdraw, 3=Deposit Cash, 4=Deposit Check")
    sys.exit(1)

# First argument = operation

try:
    inp = int(sys.argv[1])
except ValueError:
    print("Invalid operation. Please enter a number (1-4).")
    sys.exit(1)

# Second argument (optional) = amount

amount = None
if len(sys.argv) >= 3:
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        sys.exit(1)

# Match-case logic

match inp:
    case 1:
        print(" You have selected to Check Balance : ")
        print(" your current balance is : ", accBalance)
    case 2:
        print(" You have selected to Withdraw : ")
        if amount is None:
            print("Please provide an amount to withdraw.")
        elif 0 <= amount <= accBalance:
            accBalance -= amount
            print(" Please collect the cash . : ")
            print(f" Balance amount in account after transition is : {accBalance}")
        else:
            print(" Enter a valid value.The provided value is invalid ")
    case 3:
        print(" You have selected to Deposit Cash : ")
        if amount is None:
            print("Please provide an amount to deposit.")
        elif amount > 0 :
            accBalance += amount
            print(f" Balance amount in account after deposit is : {accBalance}")
        else :
            print(" Invalid deposit amount ")
    case 4:
        print(" You have selected to Deposit Check : ")
        if amount is None:
            print("Please provide an amount to deposit.")
        elif amount > 0:
            accBalance += amount
            print(f" Balance amount in account after deposit is : {accBalance}")
        else:
            print(" Invalid deposit amount ")
    case _:
        print("Invalid option selected. Please try again.")
