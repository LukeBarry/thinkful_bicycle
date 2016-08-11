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






