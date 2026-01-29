#User input values update in a set
#Code by IAH (Infinity Aggarwal Harshul)

b = int(input("Enter Value : "))   # Here we taken integer type user input value
c = int(input("Enter Value : "))
a = {                              # Here we will create a set with curly brackets
    b , c                          # Adding some values inside a set
}                                  # Closing the set with brackets
a.update({b})                      # Updating the set values with user input values
a.update({c})

print(a)                           # Then printing the updated set values

# The final output will be updated user input set values