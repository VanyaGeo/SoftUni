year = int(input()) + 1
str_year = str(year)
set_year = set(str_year)

while len(set_year) != len(str_year):
    year = year + 1
    str_year = str(year)
    set_year = set(str_year)

print(year)
