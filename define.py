#lets print the boolean using if/else using define function
# Code By IAH (Infinity Aggarwal Harshul)

Age = int(input("Enter Age: ")) # Take input from user and store it in Age variable
def is_active(Age): # Define the function is_active and store the true/false statment 
    if Age == 18: # Check if age is 18
        print("Active For Driving License") # Print if age is 18
    else:
        print("Not Active For Driving License") # Print if age is not 18
is_active(Age)  # Call the is_active function with the user's input
# #The output will show whether age is active for driving license or not using define function