# Lets Try Whether list contains palindrome of elements or not
# Code by IAH (Inifinity Aggarwal Harshul)

str1 = input("Enter Value : ")     # here we taken user input in string form
str2 = input("Enter Value : ")      
str3 = input("Enter Value : ")
str4 = input("Enter Value : ")
list = [str1,str2,str3,str4]        #here the list will store the user input value
list.copy()                         #here the above list will be copied 
list.sort()                         #here the above list will be get sorted in ascending order
print(list)                         #here the list wil get printed
if (str1 != str2 == str3 != str4) :  #here the if statment will execute the given condition
    print("Palindrome")             #now if above satement is true then palindrome will be printed
else:                               #here the else statement will execute the conditon
    print ("Not Palindrome")        #now if above statement is not true then not palindrome will be printed

#The output will be sorted user input list with a message that whether the above list is palindrome or not
#That will be decided according to the statement mentioned in the if statement

