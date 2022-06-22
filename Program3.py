n = int(input("Enter a 3 digit number="))
d1 = n//100
d2 = (n//10)%10
d3 = n % 10
s = d1 + d2 + d3
print("Sum= ",s)
