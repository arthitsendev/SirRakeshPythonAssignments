# WAP to enter 20 elements into a list and find the frequency of each elements.

lst = eval(input("Enter the elements into the list="))
l = len(lst)
u = []
c = 0
for i in range(0, l):
    e = lst[i]
    c = 1
    if e not in u:
        for j in range(i, len):
            if e == lst[j]:
                c = c + 1
            u = e
    else:
        continue
    print("Frequency of", e, "is", c)