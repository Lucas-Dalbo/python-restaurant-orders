import csv


def orders_to_dict(csv_content):
    """Função auxiliar: Transforma o csv em um dict"""
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
    """Função auxiliar: Retorna o pedido mais comum de um cliete"""
    meals = orders[customer]["meals"]
    name, times = "", 0
    print(meals)
    for meal, quant in meals.items():
        if quant > times:
            times = quant
            name = meal
    return name


def analyze_log(path_to_file: str):
    if not path_to_file.endswith(".csv"):
        raise TypeError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r", encoding="utf-8") as file:
            content = csv.reader(file, delimiter=",", quotechar="'")
            order_dict = orders_to_dict(content)

        question1 = most_ordered_meal("maria", order_dict)
        print(question1)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


analyze_log("./data/orders_1.csv")
