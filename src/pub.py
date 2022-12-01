class Pub():
    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.customers = []
        self.drinks = []
        self.customer_in_pub = 0

    #Methods:
    def get_menu(self, drinks_objects_list):
        return self.drinks

    def add_to_till(self, amount):
        self.till += amount

    def get_drinks_list_length(self):
        return len(self.drinks)

    def reduce_stock_level(self, drink_object):
        drink_object["stock"] -= 1

    def add_drinks_to_stock(self, list_of_drinks_objects):
        for drink in list_of_drinks_objects:
            self.drinks.append(drink)

    def check_steamin(self, customer):
        if customer.drunkenness > 60:
            return True
        # print("He's nae drunk yet")
        return False
    
    def check_if_underage(self, customer):
        if customer.age < 18:
            return True
        return False

    def refuse_service(self):
        print("No tonight pal.")

    def sell_drink(self, customer_object, drink_object):
        #if customer underage or drunk refuse sale
        if self.check_if_underage(customer_object) or self.check_steamin(customer_object):
            self.refuse_service
            return
        single_drink_dictionary_entry = drink_object[0]
        cost_of_drink = single_drink_dictionary_entry['price']
        strength_of_drink = single_drink_dictionary_entry["strength"]
        self.add_to_till(cost_of_drink)
        customer_object.reduce_wallet(cost_of_drink)
        customer_object.make_drunker(strength_of_drink)
        self.reduce_stock_level(single_drink_dictionary_entry)


    def sell_food(self, food_object, customer_object):
        customer_object.reduce_wallet(food_object.price)
        customer_object.rejuvenate(food_object)
    