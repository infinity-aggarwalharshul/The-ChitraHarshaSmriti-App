#Odd Number Check Loop using for loop
#Code by IAH (Infinity Aggarwal Harshul)

n = int(input("Enter the number: "))     #lest take the input from user input value
# i = 1                                    #initalize the variable equal to 1
for i in range (n):                      #while loop statment is executed every time when the variable is greater than or equal to user input value  
    if  i % 2 != 0 :                       #if the variable on division remanainder is equal to zero
        print(i)                         #print even number
        
  # The ouput will be executed every time when user input value is taken and the variable on division remanainder is
  # equal to zero or not equal to zero then it will check that it is (odd number)