#Average & Percenatage of User Input Marks with Pass & Fail Check
#Code by IAH (Infinity Aggarwal Harshul)

a = int(input("Enter Subject 1 Marks : "))  #input function will input the user value in it
b = int(input("Enter Subject 2 Marks : "))
c = int(input("Enter Subject 3 Marks : "))
d = int(input("Enter Subject 4 Marks : "))
e = int(input("Enter Subject 5 Marks : "))
f = (a+b+c+d+e)                            #additon operator will add all the numbers
s = f/5                                     #division operator will divide the sum with 5
t = ((f/500)*100)                           # here BODMASS Rule will be followed and value will be stored in a vairable
print("Average of Marks is : ",(s))         # now print will prints the output value os s variable 
print("Percentage is : " ,(t),"%")
if (t>=50) :                                #If condition will execute statement that if marks are above 50% 
    print ("pass")                           # then print pass
else :                                       # Else condition will execute if marks are below 50% 
    print ("fail")                           #then fail will be printed in the output

    #The output will be final average and percentage of marks will pass & fail check too
