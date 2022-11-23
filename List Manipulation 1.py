""" WAP to enter 20 elements in list and make two lists with the unique elements and duplicate elements
    in separate lists. """

lst = eval(input("Enter list elements="))
l = len(lst)
c = i = 0
unique = []
duplicate = []
while i < l:
    e = lst[i]
    c = 1
    if e not in unique and e not in duplicate:
        i = i + 1
        for j in range (i, l):
            if e == lst[j]:
                c = c + 1
        else:
            if c == 1:
                unique.append(e)
            else:
                duplicate.append(e)
    else:
        i = i + 1
