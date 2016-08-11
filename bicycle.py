# bicycles.py file

# Bicycles should have a model name, weight, and cost to produce
class Bicycle(object):
    def __init__(self, model, weight, cost, count):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.count = count

# Bike shops should have a store name, an inventory, sell bikes for a 20% markup above fixed cost, and can show profit
class BicycleShop(object):
    def __init__(self, store_name, inventory):
        self.store_name = store_name
        self.inventory = inventory
        self.markup = .20
        self.profit = 0


# store1.what_can_i_afford(customer1)
    def customer_afford(self, customer):
        affordable_bikes = []
        for bike in self.inventory:
            if customer.fund >= bike.cost * (1+self.markup):
                affordable_bikes.append(bike)  # list first, then append, then what you want to append
                print(customer.customer_name, "can afford a", bike.model, "bike")
        return affordable_bikes


# function that has each customer buy at least one bike and then prints the customers bicycles owned, the cost,
# and how much money they have left in their fund
    def sell(self, customer, affordable_bikes):
            bike = affordable_bikes[-1]
            customer.bicycles_owned.append(bike)
            customer.fund -= bike.cost * (1+self.markup)
            print(store1.store_name, "has", bike.count, bike.model, "bikes")
            print(customer.customer_name, "bought a", bike.model, "bike for", bike.cost * (1+self.markup))
            print(customer.customer_name, "now has", customer.fund, "in the customer fund")
            print(store1.store_name, "now has", bike.count-1, bike.model, "bikes")

# Customers should have a name, a bicycle fund, and should be able to buy bicycles
class Customers(object):
    def __init__(self, customer_name, fund):
        self.customer_name = customer_name
        self.fund = fund
        self.bicycles_owned = []

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




