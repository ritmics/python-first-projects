import random


def guess_number_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("ИГРА: Угадай число от 1 до 10!")

    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1

            if guess < secret_number:
                print("Больше!")
            elif guess > secret_number:
                print("Меньше!")
            else:
                print(f"Угадал за {attempts} попыток!")
                break

        except ValueError:
            print("Введи число!")


if __name__ == "__main__":
    guess_number_game()
    print("\nСпасибо за игру!")
