import copy
lst=[]
n=int(input("Enter number of elements :\n "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)       
print(lst)
b=copy.copy(lst)
b.sort()
print(b)
