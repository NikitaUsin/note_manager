print("Hello, world!")

struct = (["username", "Описание заметки:", "Статус заметки", "Начало день-месяц-год", "Завершение ДД.ММ.ГГ:",
           ["Заголовок 1", "Заголовок 2"]])  # вложенный список для заголовков
print(struct[0])                             # Имя пользователя
print(struct[1])                             # Содержание заметки
print(struct[2])                             # Статус
print(struct[3])                             # Дата создания
print(struct[4])                             # Дата изменения
print(struct[5])                             # ['Заголовок 1', 'Заголовок 2']

struct = input(struct[0])                    # Обращение к элементам списка
print(f"Привет,{struct[1]}!")

struct = input(struct[2])
print(f"{struct[3]}")

struct = input(struct[3])
print(f"{struct[4]}")

struct = input(struct[4])
print(f"{struct[5]}")
