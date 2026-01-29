#addtion of user input value numbers using define function
#Code by IAH (Infinity Aggarwwal Harshul)

a = int(input("Enter the number : "))   #lets take user input value 
b = int(input("Enter the number : "))
def calc_sum(a, b) :                     #now lets define function with two variables
    sum = a + b                          #Using addtion operation on two variables
    print(sum)                           #print the sum value stored with addtion of two varibles
    return a+b                           #return the sum value
calc_sum(a,b)                            #calling function with two variables outside the function to initalize the addition operation
    
#The output will be calculated as addition of two variables with user input value using define function