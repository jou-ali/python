import copy
lst=[] #user input list
n=int(input("Enter number of elements :\n ")) #Initializing the size of list
for i in range(0, n): #loop
    ele = int(input("Enter the element\t")) #taking the user input as intiger 
    lst.append(ele)       #Adding the initiger to the list
print(lst)
b=copy.copy(lst)
b.sort()
print(b)
