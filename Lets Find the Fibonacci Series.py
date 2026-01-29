# Lets Find the Fibonacci Series Using If - Elif Statment
# Code by IAH (Infinity Aggarwal Harshul)
# fibonacci series always start with 0,1 and then will be addition of first two numbers and it is 
# steadily increasing and series is {F(n) = F(n+1) + F(n+2)} (you can replace n with a simply)


a = int(input("Enter Number : "))                   #here we are taking user input value
b = 0                                               #Lets assign some value 
c = 1
a = b+c
if ((b+c)<=0) :
    print ("Error")
elif ((b+c)!=0) :
    print ("Fibonacci Series :",(b,c,(a+1),(a+2)))                         #here print function will give output according to assigned opertors

#Now the final output will show the fibonacci series