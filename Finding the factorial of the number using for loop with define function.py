#Finding the factorial of the number using for loop
#In Fcatorial concept we have to follow the formula below
#factorial of 1 =1*1 = 1 , now factorial of 2 is = 1*2*1 = 2 , same like this factorial of 3 will be 1*2*3 = 6
#same like this we can find the factorial of any numbers
#Code by IAH (Infinity Aggarwal Harshul)

n = int(input("Enter the Number : "))   #lets take an user input value
def calc_fact (n):                      #lets define a function to calculate the factorial of the number
    fact = 1                                #lets initalize the an variable as , factorial of the number equal to 1
    for i in range (1,n+1) :                #Now lets take the for loop condition in which the number will range from 1 to n+1
        fact *= i                           #taking factorial of the number equal to the factorial of the number * i
    print(fact)                         #now print the factorial of the number 
calc_fact(n)
    #The output will be show the factorial of the number with user input value using for loop condition
    