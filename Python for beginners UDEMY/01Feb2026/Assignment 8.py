num = int(input("Enter the number upto which you want to print "))
i=0
while i <= num:
    if i % 10 == 0:
        i+=1
        continue
    if i > 100:
        break
    print(i)
    i+=1