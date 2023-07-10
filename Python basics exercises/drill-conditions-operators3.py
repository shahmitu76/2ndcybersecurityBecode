#**10. Write a script that asks you to enter 2 strings
#  and displays the largest of the 2 strings (the one with the most characters).**

x=input("Enter 1st string")
y=input("Enter second string")
if len(x)<len(y):
    print(x)
else:
    print(y)