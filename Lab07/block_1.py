import pickle

def create_client_spending_dict():
    """Создает словарь с данными о клиентах и их расходах."""

    clients = {
        "Клиент А": {"январь": 1000, "февраль": 2400, "март": 1100, "апрель": 900, "май": 1500, "июнь": 1300},
        "Клиент Б": {"январь": 500, "февраль": 1000, "март": 700, "апрель": 550, "май": 800, "июнь": 650},
        "Клиент В": {"январь": 2000, "февраль": 2200, "март": 2500, "апрель": 1800, "май": 2100, "июнь": 2300},
        "Клиент Г": {"январь": 1100, "февраль": 1000, "март": 900, "апрель": 1200, "май": 1050, "июнь": 1150},
        "Клиент Д": {"январь": 800, "февраль": 900, "март": 850, "апрель": 700, "май": 1000, "июнь": 950},
        "Клиент Е": {"январь": 300, "февраль": 400, "март": 500, "апрель": 350, "май": 450, "июнь": 400},
        "Клиент Ж": {"январь": 1500, "февраль": 1600, "март": 1400, "апрель": 1700, "май": 1550, "июнь": 1650},
    }
    return clients


def analyze_client_spending(clients):
    """Анализирует расходы клиентов и выводит результаты."""

    # 1. Суммарные расходы за 6 месяцев
    total_spending = {client: sum(spending.values()) for client, spending in clients.items()}
    print("Суммарные расходы за 6 месяцев:")
    for client, total in total_spending.items():
        print(f"{client}: {total}")

    # 2. Клиент с максимальными средними расходами
    avg_spending = {client: sum(spending.values()) / len(spending) for client, spending in clients.items()}
    max_avg_client = max(avg_spending, key=avg_spending.get)
    print(f"\nКлиент с максимальными средними расходами: {max_avg_client}")

    # 3. Месяц с максимальными расходами для каждого клиента
    max_spending_month = {}
    for client, spending in clients.items():
        max_spending_month[client] = max(spending, key=spending.get)
    print("\nМесяц с максимальными расходами для каждого клиента:")
    for client, month in max_spending_month.items():
        print(f"{client}: {month}")


    # 4. Клиенты с расходами за февраль > март на 20%
    clients_feb_gt_mar = []
    for client, spending in clients.items():
        if spending.get("февраль", 0) > spending.get("март", 0) * 1.2:
            clients_feb_gt_mar.append(client)
    print("\nКлиенты с расходами за февраль > март на 20%:")
    print(clients_feb_gt_mar)

    return clients



def save_to_pickle(data, filename="data.pickle"):
    """Сохраняет словарь в бинарный файл."""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_from_pickle(filename="data.pickle"):
    """Загружает словарь из бинарного файла."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None



clients_data = create_client_spending_dict()
clients_data = analyze_client_spending(clients_data)

save_to_pickle(clients_data)

loaded_data = load_from_pickle()
if loaded_data:
    print("\nДанные из файла data.pickle:")
    analyze_client_spending(loaded_data)


