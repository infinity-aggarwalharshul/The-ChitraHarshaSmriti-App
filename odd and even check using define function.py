#Lets Check whether the number is even or odd using defined function
#Code by IAH (Infinity Aggarwal Harshul)

a = int(input("Enter Number : "))   #lets take the user input value
def check_OddEven(a):               #Lets define a function to check whether the number is even or odd and taking input from variable a and storing the result in a function
    if a % 2 == 0:                  #if variable a on division remaninder is equal to zero
        print("Even")               #then print the number is even
    else:                           #else 
        print("Odd")                #then print the number is odd
check_OddEven(a)                    #calling the function with a variable a on division remaninder

#The output will give user input value number check that whether it is even or odd using defined function