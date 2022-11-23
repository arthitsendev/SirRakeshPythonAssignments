# WAP to enter 20 elements in the list, enter a search element and find the position of the search element if any

lst = eval(input("Enter 20 elements="))
se = eval(input("Enter the search element="))
l = len(lst)
for i in range(0, l-1):
    if se == lst(i):
        print("Position= ", i)
        break