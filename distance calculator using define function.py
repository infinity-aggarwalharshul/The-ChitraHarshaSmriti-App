#Calculate distance between any two points using the distance formula using define function
# coordinates givem (x,y) and applying in the formula (x,y) = squareroot{(x2-x1)^2 - (y2-y1)^2}
#Code by IAH (Infinity Aggarwal Harshul)

import math                                                             #import the math library for mathematical formula execution

a1 = int(input("Enter x coordinate of First Point(Starting) : "))       #Lets take the user input first point starting from point  
a2 = int(input("Enter y coordinate of Final Point(Ending) : "))         #Lets take the user input final point ending from point
b1 = int(input("Enter x coordinate of Second Point (Starting) : "))     #Lets take the user input second point starting from point
b2 = int(input("Enter y coordinate of Second Point (Ending) : "))       #Lets take the user input second point ending from point

def calc_distance(a1,a2,b1,b2):                                          #lets define a function to calculate the distance between two points based on the distance between user input points
    distance = math.sqrt((b1-a1)**2 + (b2-a2)**2)                        # consider a varibale storing conversion of distance between two points inside the formula  
                                                                         #Now simply do the square root of the value stored in z variable
    return distance                                                      #returns the distance between two points
distance = calc_distance(a1, a2, b1, b2)                                 #Now, the distance variable is equal to the distance between two points function
print("The Distance will be : ", distance)                               #Now print the final value stored in z
    
#The output will be the distance between two points with user input points using the formula with define function