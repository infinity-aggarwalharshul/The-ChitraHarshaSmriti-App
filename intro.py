#Testing User Input And Storing them in the dictionary and updating them with the new user input data
#Code by IAH (Infinity Aggarwal Harshul)

Name = input("Enter Name: ")         #Enter Name using the input string
Age = int(input("Age: "))            #Enter age of the user using the int input string
Gender = input("Gender: ")           #Enter gender of the user using the input string

dict = {                             #This dictionary contains the user input data
    "Name" : "a",                    
    "Age" : "b",
    "Gender" : "c"
}

dict.update({"Name" : Name})         #now let we upadte the dictionary with the new user data
dict.update({"Age" : Age})
dict.update({"Gender" : Gender})

print(dict)                          #print the dictionary with the updated user input data

#The output dictionary which contains the user input data will show upadted user input data
