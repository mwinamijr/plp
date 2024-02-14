def calculate_discount(price, discount_percent):
	if discount_percent >= 20:
		return (price - price*discount_percent/100)

	return (price)

price = input("Please enter price: ")
discount_percent = input("Please enter discount percent: ")

print(calculate_discount(int(price), int(discount_percent)))