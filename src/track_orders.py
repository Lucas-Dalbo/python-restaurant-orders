class TrackOrders:
    def __init__(self):
        self.__orders = dict()
        self.__order_id = 1
        self.working_days = {"segunda-feira", "sabado", "terça-feira"}
        self.dishes = {"hamburguer", "pizza", "coxinha", "misto-quente"}

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.__orders)

    def __customer_filter(self, customer, filter):
        orders = self.get_customer_orders(customer)
        dishes_set = set()
        for order in orders:
            cust = order["name"]
            if cust == customer:
                dishes_set.add(order[filter])
        return dishes_set

    def get_customer_orders(self, customer):
        orders = self.__orders.values()
        customer_orders = []
        for order in orders:
            if order["name"] == customer:
                customer_orders.append(order)
        return customer_orders

    def add_new_order(self, customer, order, day):
        new_order = {"name": customer, "dish": order, "day": day}
        self.__orders[self.__order_id] = new_order
        self.__order_id += 1

    def get_most_ordered_dish_per_customer(self, customer):
        orders = self.get_customer_orders(customer)
        dish_name, times = "", 0
        meals_quant = {}
        for order in orders:
            dish = order["dish"]
            if dish not in meals_quant:
                meals_quant[dish] = 1
            else:
                meals_quant[dish] += 1
            if meals_quant[dish] > times:
                times = meals_quant[dish]
                dish_name = dish
        return dish_name

    def get_never_ordered_per_customer(self, customer):
        cus_dishes = self.__customer_filter(customer, "dish")
        never_ordered = self.dishes.difference(cus_dishes)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        visited_days = self.__customer_filter(customer, "day")
        never_came_on = self.working_days.difference(visited_days)
        return never_came_on

    def __days_balance(self):
        balance = dict()
        for order in self.__orders.values():
            day = order["day"]
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
