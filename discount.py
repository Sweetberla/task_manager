# Ask user to input their purchase amount as float
amount = float(input("what is your purchase amount "))
# If the purchase is 100 cedis or more apply 20% discount and print amount to pay
if amount >= 100:
    discount = amount * 0.2
    total_after_discount = amount - discount
    print(f"amount to pay: {total_after_discount}")
# If the purchase is 50 cedis or more apply 10% discount and print amount to pay
elif amount >= 50 and amount <= 99.99:
    discount = amount * 0.1
    total_after_discount = amount - discount
    print(f"amount to pay: {total_after_discount}")
# If the purchase is less than 50 cedis apply no discount and print amount to pay
elif amount < 50:
    print(f"amount to pay: {amount}")


 