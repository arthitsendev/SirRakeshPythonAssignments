# WAP to enter 10 elements into 2 lists and merge both list elements into 3rd list alternatively.

lst1 = eval(input("Enter the elements of first list="))
lst2 = eval(input("Enter the elements of second list="))
lst3 = []
for i in range(0, 20, 2):
    lst3[i].append(lst1[i])
    lst3[i+1].append(lst2[i])
print(lst3)