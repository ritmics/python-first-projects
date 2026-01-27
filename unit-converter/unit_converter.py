history = []

while True:
    print("\n=== УМНЫЙ КОНВЕРТЕР ===")
    print("1. Температура")
    print("2. Длина")
    print("3. Вес")
    print("4. История конвертаций")
    print("0. Выход")

    choice = input('Ваш выбор: ')

    if choice == "1":
        print("\nТемпература:")
        print("1. C° → F°")
        print("2. F° → C°")
        print("3. Назад")

        temp_choice = input('Выбор: ')
        if temp_choice == "1":
            c = float(input('Градусы Цельсия: '))
            f = (c * 9 / 5) + 32
            print(f"Результат: {c}°C = {f:.1f}°F")
            history.append(f"Температура: {c}°C = {f:.1f}°F")

        elif temp_choice == "2":
            f = float(input('Градусы Фаренгейта: '))
            c = (f - 32) * 5 / 9
            print(f"Результат: {f}°F = {c:.1f}°C")
            history.append(f"Температура: {f}°F = {c:.1f}°C")

        elif temp_choice == "3":
            continue

    elif choice == "2":
        print('\nДлина:')
        print("1. Метры → Километры")
        print("2. Километры → Метры")
        print("3. Назад")

        km_choice = input('Выбор: ')
        if km_choice == "1":
            m = float(input('Метры: '))
            km = m / 1000
            print(f"Результат: {m} м = {km} км")
            history.append(f"Длина: {m} м = {km} км")

        elif km_choice == "2":
            km = float(input('Километры: '))
            m = km * 1000
            print(f"Результат: {km} км = {m} м")
            history.append(f"Длина: {km} км = {m} м")

        elif km_choice == "3":
            continue

    elif choice == "3":
        print('\nВес:')
        print('1. Килограммы → Граммы')
        print('2. Граммы → Килограммы')
        print('3. Назад')

        kg_choice = input('Выбор: ')
        if kg_choice == "1":
            kg = float(input('Килограммы: '))
            g = kg * 1000
            print(f'Результат: {kg} кг = {g} г')
            history.append(f"Вес: {kg} кг = {g} г")

        elif kg_choice == "2":
            g = float(input('Граммы: '))
            kg = g / 1000
            print(f"Результат: {g} г = {kg} кг")
            history.append(f"Вес: {g} г = {kg} кг")

        elif kg_choice == "3":
            continue

    elif choice == "4":
        print("\n=== ИСТОРИЯ КОНВЕРТАЦИЙ ===")
        if not history:
            print("История пуста")
        else:
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")

    elif choice == "0":
        print("Выход из программы. До свидания!")
        break

    else:
        print("Неверный выбор! Попробуйте снова.")