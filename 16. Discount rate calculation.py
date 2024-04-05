def discount(price, rate):
    discount_rate = price * (rate / 100)
    discounted = price - discount_rate
    print(f"Discounted price: {discounted}")

discount(50,5)