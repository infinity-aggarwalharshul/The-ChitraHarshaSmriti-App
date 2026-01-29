#Finding the factorial of the number using while loop
#In Fcatorial concept we have to follow the formula below
#factorial of 1 =1*1 = 1 , now factorial of 2 is = 1*2*1 = 2 , same like this factorial of 3 will be 1*2*3 = 6
#same like this we can find the factorial of any numbers
#Code by IAH (Infinity Aggarwal Harshul)

n = int(input("Enter the Number : "))     #lets take the user input value from the user
fact = 1                                  #lets initalize the factorial of the number equal to the 1
i = 1                                     #lets initalize a variable equal to 1                      
while i <= n:                             # using while loop we will take an condition if an variable is equal to user input value
    fact *= i                             #taking factorial of the number equal to the factorial of the number * i
    i += 1                                #now increment the variable with 1
    print(fact)                           #print the factorial of the number
    
    #The output will show the factorial of the number with user input value using while loop