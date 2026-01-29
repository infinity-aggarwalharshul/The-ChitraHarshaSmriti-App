#tranverse of tuple with user input value using for loop
#code by IAH (Infinity Aggarwal Harshul)

x = int(input("Enter Number : "))   #here we take any user input value
a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)   #lets take an example tuple list

for i in range(len(a)):                  # now in for loop we taken a condition if variable is les100s than length of tuple
    print("Checking :", a[i])
    if a[i] == x :                # lets take one more condition if tuple at any index is equal to user input value
        print("Found At Inx : ",i)  # then print found
        break                       #break statement used to stop the execution( like a car break type) after founding the user input value in the example list
else :                          #lets take else condition which will show if above statement is not true then find untill it reaches tuple length limit
    print("Value not Found in tuple")       # now simply print finding uptill value gets finded inside tuple 
    # i += 1                          # for loop we dont require this statment so we comment it out (increment it by 1)
print ("end of loop")               #now after finding the value print end of loop

#The output will be finding user input value in example tuple and when value will be found 
#it will come out from loop and will stop the execution because of break statement used for it
# And if we enter any value outside the example tuple then will find and after reaching length 
#tuple it will end the loop