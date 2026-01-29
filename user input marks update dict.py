# making user input marks update dictionary
#code by IAH (infinity Aggarwal Harshul)

a = int(input("Enter Phy Marks :"))    # here user will input any integer value 
b = int(input("Enter Chem Marks :"))
c = int(input("Enter Maths Marks :"))

s = {                                    #creating a dictionary of various subjects 
    "Phy" : "a",                         #listing all subject name as keys and taking a variable on other side
    "Chem" : "b",
    "Maths" : "c"
}                                        # dictionary get closed with curly brackets
s.update({"Phy" :a})                     # update function will simply update the values of dictionary with user input values
s.update({"Chem" :b})
s.update({"Maths" :c})

print(s)                                 # here we can then print the updated dictionary

# The Output will final updated dictionary with user input values