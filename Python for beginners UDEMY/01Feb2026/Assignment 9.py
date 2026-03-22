num = int(input("Enter the number you want to check "))
primeFlag = True
for i in range(2,int(num+1/2)):
    if num % i == 0:
        primeFlag = False
if primeFlag:
    print("The number is prime")
else:
    print("The number is not prime")