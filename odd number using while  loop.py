#Odd Number Check Loop using while loop
#Code by IAH (Infinity Aggarwal Harshul)

n = int(input("Enter the number: "))  #lest take the input from user input value
i = 1                                  #initalize the variable equal to 1
while i <=n:                          #while loop statment is executed every time when the variable is greater than or equal to user input value  
    if (i%2 != 0):                     #if the variable on division remanainder is equal to zero
        print(i)                         #print odd number
        i += 1
    else:                              #else if the variable on division remanainder is not equal to zero
        print(i)                        #print odd number
    i += 1                             #increment by varialble by 1
        
  # The ouput will be executed every time when user input value is taken and the variable on division remanainder is
  # equal to zero or not equal to zero then it will check that it is (odd number)
