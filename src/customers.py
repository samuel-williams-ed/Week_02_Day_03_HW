class Customers():
    def __init__(self, input_name, input_age, input_drunkenness, input_wallet):
        self.name = input_name
        self.age = input_age
        self.drunkenness = input_drunkenness #int
        self.wallet = input_wallet
    #methods:

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def make_drunker(self, drink_object):
        #take drunkness int from drink class and add to drunkenenesss
        amount_of_alchol = drink_object #int
        self.drunkenness += amount_of_alchol #int
    
    def rejuvenate(self, food_object):
        self.drunkenness -= food_object.rejuvenation_level
        # print(f"Rejuvenating the customer {food_object.rejuvenation_level}")
    