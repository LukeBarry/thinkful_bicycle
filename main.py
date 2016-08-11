from bicycle.import

# main.py file
print("watch this video https://www.youtube.com/watch?v=th3QlxeGoP0")

bike1 = Bicycle("kid", "10 lbs", 100, 10)
bike2 = Bicycle("standard", "40 lbs", 150, 10)
bike3 = Bicycle("bmx", "30 lbs", 200, 10)
bike4 = Bicycle("mountain", "50 lbs", 250, 10)
bike5 = Bicycle("racing1", "20 lbs", 300, 10)
bike6 = Bicycle("racing2", "10 lbs", 600, 10)
all_bikes = [bike1, bike2, bike3, bike4, bike5, bike6, 10]

store1 = BicycleShop("luke's", {bike1: 10, bike2: 10, bike3: 10, bike4: 10, bike5: 10, bike6: 10})

customer1 = Customers("Joe", 200)
customer2 = Customers("Jack", 500)
customer3 = Customers("John", 1000)
all_customers = [customer1, customer2, customer3]


# Print customer name and call the new method of the store1 object
for customer in all_customers:
    print(customer.customer_name)
    affordable = store1.customer_afford(customer)  # passed a new variable into the return of the affordable function
    store1.sell(customer, affordable)
    