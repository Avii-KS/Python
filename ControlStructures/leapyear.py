year=int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:    
    print(f"{year} has 366 days")
else:
    print(f"{year} has 365 days")