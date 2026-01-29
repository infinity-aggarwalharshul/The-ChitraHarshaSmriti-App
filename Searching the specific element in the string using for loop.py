#Searching the specific element in the string using for loop
#Code by IAH (Infinity Aggarwal Harshul)

str = "This is my test code line text"      #lets take an string where a sentence is taken
for char in str :                           #now lets consider for loop and will try to find characters in the  string
    if (char == 't') :                      #if character is equal to 't' then it means that  character is in the string
        print("x found",str[27],len(str))   # print the statement of character founded in the string & also print its length and character at specific index defined inside the string
        break                               #break statement is used to end the loop
    print (char)                            #print the statement of character
else:                                       #here else statement is used 
 print("end of loop")                       #print the end of loop statement to end the loop with this statement
    
    #In the output we will see the print of a speciific character using for loop
    #will be checking that character is in the string or not if yes the it will get printed