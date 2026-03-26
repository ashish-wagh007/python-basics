wage = float(input("Hourly wage: "))
work = float(input("Hours worked: "))
day = input("Day of the week: ")
dailywage = (wage * work)
if day == ("Sunday"):
    dailywage = (wage * work) * 2
print(f"Daily wages: {dailywage} euros")
