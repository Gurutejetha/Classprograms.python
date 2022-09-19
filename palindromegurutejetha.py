a=int(input("enter a number to check if it is a palindrome or not"))
rev=0
rev=int(str(a)[::-1])
if(a==rev):
    print("palindrome")
else:
    print("not a palindrome")
