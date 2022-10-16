money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
grow = 1.05
delta = salary - spend
while money_capital + delta >= spend:
    money_capital += delta
    spend = spend * grow

    month += 1

print(month)
