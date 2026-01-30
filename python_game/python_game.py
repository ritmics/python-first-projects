questions = [
    {
        "question": "Какая функция выводит текст в Python?",
        "options": ["1. print()", "2. input()", "3. len()", "4. str()"],
        "answer": 1
    },
    {
        "question": "Какой тип данных изменяемый в Python?",
        "options": ["1. str", "2. tuple", "3. list", "4. int"],
        "answer": 3
    },
    {
        "question": "Что выведет print(2 + 2 * 2)?",
        "options": ["1. 6", "2. 8", "3. 4", "4. Ошибка"],
        "answer": 1
    }
]

score = 0

print("=== ПРИВЕТ! ЭТО ВИКТОРИНА ПО PYTHON ===\n")

for i in range(len(questions)):
    print(f"Вопрос {i + 1}:")
    print(questions[i]["question"])

    for option in questions[i]["options"]:
        print(option)

    user_answer = int(input("Ваш ответ (введите номер): "))

    if user_answer == questions[i]["answer"]:
        print("Правильно!\n")
        score += 1
    else:
        print(f"Неправильно. Правильный ответ: {questions[i]['answer']}\n")

percentage = (score / len(questions)) * 100

print("=" * 30)
print(f"ВАШ РЕЗУЛЬТАТ: {score} из {len(questions)}")
print(f"Процент правильных: {percentage:.1f}%")

if percentage == 100:
    print("ИДЕАЛЬНЫЙ РЕЗУЛЬТАТ!")
elif percentage >= 70:
    print("ОТЛИЧНО!")
elif percentage >= 50:
    print("ХОРОШО!")
else:
    print("ПОПРОБУЙТЕ ЕЩЁ РАЗ!")