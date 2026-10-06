# [ ] create fucntion, call and test 

def cheese_order(order_amount, max_order=100, min_order=0.25, price=7.99):
    order_amount = float(order_amount)
    max_order = float(max_order)
    min_order = float(min_order)
    price = float(price)

    if order_amount > max_order:
        print(str(order_amount) + " is more than currently available stock")
    elif order_amount < min_order:
        print(str(order_amount) + " is below minimum order amount")
    else:
        total_price = order_amount * price
        print(str(order_amount) + " costs $" + format(total_price, ".2f"))


order = input("Soraja Omanovic, enter cheese order weight (numeric value): ")
cheese_order(order)