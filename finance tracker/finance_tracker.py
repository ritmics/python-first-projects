from datetime import datetime

transactions = []
balance = 0


def show_menu():
    print("\n=== ФИНАНСОВЫЙ ТРЕКЕР ===")
    print("1. Добавить доход")
    print("2. Добавит расход")
    print("3. Показать баланс")
    print("4. История операций")
    print("5. Статистика по категориям")
    print("0. Выход")


while True:
    show_menu()
    choice = input("Выбор: ")

    if choice == "1":
        category = input("Категория дохода (например: зарплата, подарок): ")
        amount = int(input("Сумма: "))
        transactions.append({
            "type": "доход",
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

        balance += amount
        print(f"Добавлен доход: {amount} руб ({category})")
    elif choice == "0":
        break
    elif choice == "2":
        category = input("Категория расхода (например: еда, транспорт): ")
        amount = int(input("Сумма: "))

        transactions.append({
            "type": "расход",
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        })
        balance -= amount
        print(f"Добавлен расход: {amount} руб ({category})")
    elif choice == "3":
        print(f'Ваш баланс: {balance} руб')
    elif choice == "4":
        print("\n=== ИСТОРИЯ ОПЕРАЦИЙ ===")

        if not transactions:
            print("Операций пока нет")
        else:
            for i, op in enumerate(transactions, 1):
                if op["type"] == "доход":
                    print(f"{i}. {op['date']} - {op['category']} +{op['amount']} руб")
                else:
                    print(f"{i}. {op['date']} - {op['category']} -{op['amount']} руб")
    elif choice == "5":
        print("\n=== СТАТИСТИКА ПО КАТЕГОРИЯМ ===")

        if not transactions:
            print("Нет операций для статистики")
            continue

        stats = {}
        for op in transactions:
            cat = op["category"]
            if cat not in stats:
                stats[cat] = 0

            if op["type"] == "доход":
                stats[cat] += op["amount"]
            else:
                stats[cat] -= op["amount"]

        for category, total in stats.items():
            print(f"{category}: {total:+} руб")
