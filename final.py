print("Hello, world!")

username = input("Введите ваше ФИО")
content = input("Описание")
status = input("Готовность задачи")
created_date = input("Начало ДД.ММ.ГГ:")
issue_date = input("Завершение ДД.ММ.ГГ:")
temp_issue_date = input("Изменение :")
temp_created_date = input("Дедлайн :")

struct = ([username, content, status, created_date, issue_date,
           [temp_issue_date, temp_created_date]])  # вложенный список для заголовков

print(f"Введите ваше ФИО: struct [0]")
print(f"Описание: struct [1]")
print(f"Готовность задачи: struct [2]")
print(f"Начало ДД.ММ.ГГ: struct [3]")
print(f"Завершение ДД.ММ.ГГ: struct [4]")
print(f"Изменение : struct [5]")
print(f"Дедлайн : struct [6]")
