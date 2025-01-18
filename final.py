print("Hello, world!")

struct = (["Имя пользователя", "Содержание заметки", "Статус", "Дата создания", "Дата изменения",
           ["Заголовок 1", "Заголовок 2"]])  # вложенный список для заголовков
print(struct[0])                             # Имя пользователя
print(struct[1])                             # Содержание заметки
print(struct[2])                             # Статус
print(struct[3])                             # Дата создания
print(struct[4])                             # Дата изменения
print(struct[5])                             # ['Заголовок 1', 'Заголовок 2']

struct = input(struct[0])                    # Обращение к элементам списка
print(f"{struct[0]}")

struct = input(struct[1])
print(f"{struct[1]}")
