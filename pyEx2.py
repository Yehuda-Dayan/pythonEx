# Exercise 1: salary Breakdown
gross_salary = float(input("enter your salary: "))
net_income = gross_salary - ( gross_salary * 0.22 )
print("Your net income is", net_income)
if net_income > 3000:
    print("You have enough money for rent")
else:
    print("You don't have enough money for rent")
reminder_after_rent = net_income - 3000
if reminder_after_rent >= 1000:
        print("Rent and save")
elif reminder_after_rent < 1000 and reminder_after_rent >= 0:
        print("just rent")
elif reminder_after_rent < 0:
        print("WOMP WOMP")