countries = input().split(", ")
capitals = input().split(", ")
# country_capital_dict = {countries[index]: capitals[index] for index in range(len(capitals))}
country_capital_dict = dict(zip(countries, capitals)) # 3-ти и 4-ти ред извършват едно и също действие
for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")


# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London