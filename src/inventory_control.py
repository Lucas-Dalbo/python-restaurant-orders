from track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = TrackOrders()
        self.invetory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, customer, order, day):
        ingredients = self.INGREDIENTS[order]
        for ing in ingredients:
            if self.invetory[ing] == 0:
                return False
            self.invetory[ing] -= 1
        self.orders.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        to_buy = {}
        for item, quant in self.invetory.items():
            dif = self.MINIMUM_INVENTORY[item] - quant
            if dif > 0:
                to_buy[item] = dif
            else:
                to_buy[item] = 0
        return to_buy

    def get_available_dishes(self):
        dishes = set()
        for dish, ingr in self.INGREDIENTS.items():
            is_avaliable = True
            for i in ingr:
                if self.invetory[i] < 1:
                    is_avaliable = False
                    break
            else:
                if is_avaliable:
                    dishes.add(dish)
        return dishes
