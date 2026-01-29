# Here is the Georgian Calendar & Leap Year Program
#Code by IAH (Infinity Aggarwal Harshul)

year = int(input("Enter Year : "))        #taking the user input value
leap = True                               #storing true statement in a variable
leap1 = False

if (year%4==0) :                           # Using if statment means if this statement is true
    print ("Leap Year")                    #Then Print it is leap year
elif (year%100==0) :                       # Using elif statement to decide else/if the statement is false
    print ("Not Leap Year")                #Then Print it is not leap year
elif (year%400==0) :                       # Using Again else/if statement to decide if this statement is true
    print ("Leap Year")                    #Then also Print it is leap year
else :                                     # Using the else statement to decide if all above statement is not true 
    print("Not Leap Year")                 #Then Print it is not leap year

# The Output will give the final answer according to the statement that whether it is leap year or not

