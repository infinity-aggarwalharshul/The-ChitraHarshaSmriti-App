#smallest of four numbers
#code by IAH (Infinity Aggarwal Harshul)

a = int(input("Enter Num : "))
b = int(input("Enter Num2 : "))
c = int(input("Enter Num3 : "))
d = int(input("Enter Num4 : "))
if (a<b and a<c and a<d) :               #if statement is a conditonal operator that tells condition is acceptable or not
    print ("Smallest is ",a)             #prints the command written inside it
elif (b<c and b<d):                      #elif statement is a combination of both else and if statement and checks multiple conditions
    print ("Smallest is ",b)
elif (c<d) :                             #opposite of if statement it can check the opposite part of statement  print ("Greatest is ",c)
    print ("Smallest is ",c)
else :
    print ("Smallest is ",d)

    # if the if statement stores true value then else statement will store false value
    # And vice versa is also possible
# the output will be smallest of four numbers as per user input assigned value