days = int(input("Enter the total number of days="))
years = days / 365
months = (days - (years * 365))/30
d = days - ((years * 365)+(months * 30))
print(years," years",months," months",d," days")
