day = 0
savings = 0

while day < 365:
	day += 1
	savings += day * 0.5
	amount = day * 0.5
	current_savings = savings
	print("Day of the Year:")
	print(day)
	print("Amount Added:")
	print(amount)
	print("Current Savings:")
	print(current_savings)
	print("-----")

else:
	print("Year's savings:")
	print(current_savings)
	print("Congrats! That's a lot of money!")
