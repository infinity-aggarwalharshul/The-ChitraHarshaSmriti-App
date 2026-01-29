#Calculating Average with User Input Value
#Code by IAH(Infinity Aggarwal Harshul) 

a = int(input("Enter the number : "))    #Lets take the input with user input value
b = int(input("Enter the number2 : "))
c = int(input("Enter the number3 : "))
def calc_avg(a, b, c):                  #Defining the Average function with three varibles
    sum = a + b + c                     #Lets take a sum of the three varibles
    avg = sum / 3                       #lets take average of sum of the three varibles divided by total number of variables
    print(avg)                          #print the average of the three varibles
    return avg                          #return the average of the three varibles
calc_avg(a, b, c)                       #Lets call the Average function with three varibles

#The output will show the average of the three numbers with user input value using the define function
