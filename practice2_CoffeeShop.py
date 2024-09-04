# Write a class called CoffeeShop, which has three instance variables:
# name : a string (basically, of the shop)
# menu : a list of items (of dict type), with each item containing the item (name of the item),
# type (whether a food or a drink) and price.
# orders : an empty list
# and seven methods:
# add_order: adds the name of the item to the end of the orders list if it exists on the menu, otherwise,
# return "This item is currently unavailable!"
# fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty,
# return "All orders have been fulfilled!"
# list_orders: returns the item names of the orders taken, otherwise, an empty list.
# due_amount: returns the total amount due for the orders taken.
# cheapest_item: returns the name of the cheapest item on the menu.
# drinks_only: returns only the item names of type drink from the menu.
# food_only: returns only the item names of type food from the menu.
# IMPORTANT: Orders are fulfilled in a FIFO (first-in, first-out) order. Examples:

class CoffeeShop:
    def __init__(self, shop_name, menu):
        self.name = shop_name
        self.menu = menu

    def show (self):
        for item in self.menu:
            print(item['item_name'])

tcs = CoffeeShop ("Tesha's coffee shop",[{'item_name': "orange juice", 'type': "drink"},
                                         # ])
                                          {'item_name': "lemonade", 'type': "drink"},
                                          {'item_name': "cranberry juice", 'type': "drink"},
                                          {'item_name': "hot chocolate", 'type': "drink"},
                                          {'item_name': "vanilla chai latte", 'type': "drink"},
                                          {'item_name': "pineapple juice", 'type': "drink"},
                                          {'item_name': "lemon iced tea", 'type': "drink"},
                                          {'item_name': "iced coffee", 'type': "drink"}])

tcs.show()