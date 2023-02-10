import csv


def orders_to_dict(csv_content):
    """Função auxiliar:
    Transforma o csv em um dict"""
    order_list = list(csv_content)
    order_dict = {}
    for name, meal, day in order_list:
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
    return order_dict


def most_ordered_meal(customer: str, orders: dict):
    """Função auxiliar:
    Retorna o pedido mais comum de um cliete"""
    meals = orders[customer]["meals"]
    name, times = "", 0
    for meal, quant in meals.items():
        if quant > times:
            times = quant
            name = meal
    return name


def times_ordered(customer: str, meal: str, orders: dict):
    """Função auxiliar:
    Retorna quantas vezes um pedido foi feito pelo cliente"""
    result = orders[customer]["meals"][meal]
    return result


def get_all_meals(orders: dict):
    """Função auxiliar:
    Retorna o menu segundo os pedidos feitos"""
    all_meals = set()
    for key in orders:
        meals = set(orders[key]["meals"].keys())
        all_meals = all_meals.union(meals)
    return all_meals


def never_ordered_meals(customer: str,  orders: dict):
    """Função auxiliar:
    Retorna os itens que nunca foram pedidos pelo cliente"""
    all_meals = get_all_meals(orders)
    cus_meals = set(orders[customer]["meals"].keys())
    never_ordered = all_meals.difference(cus_meals)
    return never_ordered


def working_days(orders: dict):
    """Função auxiliar:
    Retorna os dias de trabalho"""
    w_days = set()
    for key in orders:
        days = orders[key]["days"]
        w_days = w_days.union(days)
    return w_days


def never_came(customer: str,  orders: dict):
    """Função auxiliar:
    Retorna os itens que nunca foram pedidos pelo cliente"""
    w_days = working_days(orders)
    visited_days = orders[customer]["days"]
    never_came = w_days.difference(visited_days)
    return never_came


def analyze_log(path_to_file: str):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            content = csv.reader(file, delimiter=",", quotechar="'")
            order_dict = orders_to_dict(content)

        question1 = most_ordered_meal("maria", order_dict)
        question2 = times_ordered("arnaldo", "hamburguer", order_dict)
        question3 = never_ordered_meals("joao", order_dict)
        question4 = never_came("joao", order_dict)

        with open("./data/mkt_campaign.txt", "w", encoding="utf-8") as file:
            file.write(f"{question1}\n")
            file.write(f"{question2}\n")
            file.write(f"{question3}\n")
            file.write(f"{question4}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
