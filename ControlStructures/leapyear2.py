import calendar

def year_days(year):
    num_days = calendar.isleap(year) and 366 or 365
    return f"{year} has {num_days} days"

# Example usage:
input_year = 2000
result = year_days(input_year)
print(result)