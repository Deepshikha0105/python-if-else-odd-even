n= input(int("enter the number:")
if n%2!=0:
    print("Weird")
if n%2==0: 
    if n>2 and n<6:
        print("Not Weird")
    if n in range(6,21):
        print("Weird")
    if n>20:
        print("Not Weird")
