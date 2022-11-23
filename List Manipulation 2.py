# WAP to enter 10 elements in 2 lists and display after  and before swap of list elements.

lst1 = eval(input("Enter the elements of first list="))
lst2 = eval(input("Enter the elements of second list="))
t = lst2
l1 = len(lst1)
l2 = len(lst2)
print(lst1, lst2)
for i in range(0, 10):
    lst2[i] = lst1[i]
    lst1[i] = t[i]
print("After swapping elements=")
print(lst1, lst2)