import collections

# Словарь для хранения информации о питомцах
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 14,
            "Имя владельца": "Саша"
        }
    },
}

# Функция для определения правильного окончания для возраста питомца
def get_suffix(age):
    if age == 1:
        return "год"
    elif 1 < age < 5:
        return "года"
    else:
        return "лет"

# Функция для создания нового питомца
def create():
    print("### Комманда create")

    key = input("Кличка питомца: ")

    fields = ["Вид питомца", "Возраст питомца", "Имя владельца"]

    temp = {key: dict()}

    for field in fields:
        res = input(f"{field}: ")
        temp[key][field] = int(res) if field == "Возраст питомца" and res.isnumeric() else res

    last = collections.deque(pets, maxlen=1)[0]  # Получаем последний ключ в словаре
    pets[last + 1] = temp  # Добавляем новую запись в словарь

# Функция для чтения информации о питомце
def read():
    print("### Комманда read")
    ID = int(input("Введите ID: "))
    pet = pets.get(ID)  # Получаем информацию о питомце по ID

    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
    else:
        key = list(pet.keys())[0]
        pet_info = pet[key]
        age_suffix = get_suffix(pet_info["Возраст питомца"])
        print(f'Это {pet_info["Вид питомца"]} по кличке "{key}". Возраст питомца: {pet_info["Возраст питомца"]} {age_suffix}. Имя владельца: {pet_info["Имя владельца"]}')

# Функция для обновления информации о питомце
def update():
    print("### Комманда update")
    ID = int(input("Введите ID: "))
    pet = pets.get(ID)  # Получаем информацию о питомце по ID

    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
    else:
        key = list(pet.keys())[0]
        print("Введите данные или оставьте поле пустым для сохранения текущих значений:")
        for field, value in pet[key].items():
            new_value = input(f"{field} ({value}): ")
            if new_value:
                pet[key][field] = int(new_value) if field == "Возраст питомца" and new_value.isnumeric() else new_value

# Функция для удаления питомца
def delete():
    print("### Комманда delete")
    ID = int(input("Введите ID: "))
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID: {ID} удален")
    else:
        print(f"Питомца с ID:{ID} не существует")

# Функция для получения информации о питомце по ID
def get_pet(ID):
    pet = pets.get(ID)
    return pet

# Основная часть программы
while True:
    print("""
    Меню:
    1. Создать питомца
    2. Прочитать информацию о питомце
    3. Обновить информацию о питомце
    4. Удалить питомца
    5. Выйти
    """)

    choice = input("Выберите действие: ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Неправильный выбор. Попробуйте еще раз.")