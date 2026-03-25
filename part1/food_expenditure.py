que1 = int(input("How many times a week do you eat at the cafeteria? "))
que2 = float(input("The price of a typical student lunch? "))
que3 = float(input("How much money do you spend on groceries in a week? "))
weekly_total = que1 * que2 + que3
print("Average food expenditure:")
print(f"Daily: {weekly_total/7} euros")
print(f"Weekly: {weekly_total} euros")
