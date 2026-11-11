print("Electricity Bill Category")
consumption = input("Monthly Electricity Consumption: ")

consumption=int(consumption)
if 0 < consumption < 100 :
    print("Low Consumption")
elif 99 < consumption < 300 :
    print("Moderate Consumption")
elif 299 < consumption < 500 :
    print("High Consumption")
else :
    print("Very High Consumption")