  #*(removing constant from vowels list and then sorting the final list in ascending order)
  #code by IAH (Infinity Aggarwal Harshul)  
#index=["0","1","2","3","4","5","6"]     #here is the index numbering of below vowels & constant mix list
list = ["a","e","i","y","o","t","u"]       #here is list of vowels with constants mix
list.pop(3)                                # this will remove any value/character on a specific index
list.remove("t")                             #this will remove that value assigned on a specific index
list.sort()                                #this will sort the list in ascending order
print (list)                               #this will print the string form of list

#the final putput will be a sorrted list in ascending order with vowels only 