class TrackOrders:
    def __init__(self):
        self.__orders = list()
        self.__dict_orders = dict()
        self.working_days = {"segunda-feira", "sabado", "terça-feira"}
        self.meals = {"hamburguer", "pizza", "coxinha", "misto-quente"}

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.__orders)
    
    def __orders_to_dict(self):
        order_dict = {}
        for name, meal, day in self.__orders:
            if name not in order_dict:
                order_dict[name] = {
                    "meals": {meal: 1},
                    "days": set()
                }
            else:
                if meal not in order_dict[name]["meals"]:
                    order_dict[name]["meals"][meal] = 1
                else:
                    order_dict[name]["meals"][meal] += 1
            order_dict[name]["days"].add(day)
        self.__dict_orders = order_dict

    def add_new_order(self, customer, order, day):
        new_order = [customer, order, day]
        self.__orders.append(new_order)
        self.__orders_to_dict()

    def get_most_ordered_dish_per_customer(self, customer):
        meals = self.__dict_orders[customer]["meals"]
        name, times = "", 0
        for meal, quant in meals.items():
            if quant > times:
                times = quant
                name = meal
        return name

    def get_never_ordered_per_customer(self, customer):
        cus_meals = set(self.__dict_orders[customer]["meals"].keys())
        never_ordered = self.meals.difference(cus_meals)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        visited_days = self.__dict_orders[customer]["days"]
        never_came_on = self.working_days.difference(visited_days)
        return never_came_on
    
    def __days_balance(self):
        balance = dict()
        for _, _, day in self.__orders:
            if day not in balance:
                balance[day] = 1
            else:
                balance[day] += 1
        return balance

    def get_busiest_day(self):
        balance = self.__days_balance()
        most = max(balance.values())
        for day in balance:
            if balance[day] == most:
                return day

    def get_least_busy_day(self):
        balance = self.__days_balance()
        least = min(balance.values())
        for day in balance:
            if balance[day] == least:
                return day