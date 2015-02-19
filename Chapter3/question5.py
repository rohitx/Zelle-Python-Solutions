def main():
    wt = input("Please enter the number of orders in pounds: ")
    coffee_cost = wt * 10.50
    shipping_cost = wt * 0.86 + 1.50
    total_cost = coffee_cost + shipping_cost
    print 'Your total cost is: {tc:.2f}'.format(tc=total_cost)

main()