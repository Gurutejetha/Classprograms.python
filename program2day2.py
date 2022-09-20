year = int(input("Enter the Year to be checked: "))
if (year%400 == 0):
          print("Leap Year")
elif (year%100 == 0):
          print("Not the Leap Year")
elif (year%4 == 0):
          print("a Leap Year")
else:
          print("Not the Leap Year")
