""" WAP to enter 20 numbers into a list and find the maximum element from first half and minimum element from second half
of the list """

lst = eval(input("Enter the elements="))
h = 0
s = lst[10]
for i in range(0, 10):
    if lst[i] > h:
        h = lst[i]
    print("Maximum element=", h)
for i in range(10, 20):
    if lst[i] < s:
        s = lst[i]
    print("Minimum element=", s)
