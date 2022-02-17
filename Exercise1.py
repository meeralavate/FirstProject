"""
1. Write a simple python program which will take one string input parameter as command line argument.
Verify if the last character of the string is Capital Letter. For e.g. If we pass “AbcD” as command line argument,
then output should be true and for “Abcd” output would be false.
"""
# Taking input from the user
str = input()
 
# Output
print(str)

for char in str[-1]:
    k = char.isupper()  
    if k == True:
        print(True)
    else:
	    print(False)

