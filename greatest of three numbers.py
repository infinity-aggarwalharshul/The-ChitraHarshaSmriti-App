#greatest of three numbers
#code by IAH (Infinity Aggarwal Harshul)

a = int(input("Enter Num :"))
b = int(input("Enter Num2 :"))
c = int(input("Enter Num3 : "))
if (a>b and a>c) :               #if statement is a conditonal operator that tells condition is acceptable or not
    print ("Greatest is ",a)     #prints the command written inside it
elif (b>c):                      #elif statement is a combination of both else and if statement and checks multiple conditions
    print ("Greatest is ",b)
else :                           #opposite of if statement it can check the opposite part of statement  print ("Greatest is ",c)
    print ("Greatest is ",c)

    # if the if statement stores true value then else statement will store false value
    # And vice versa is also possible
# the output will be greatest of three numbers as per user input 