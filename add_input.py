print("Hello, world!")

username = input("Введите ваше ФИО")         # Ввод имени
title = input("Введите заголовок заметки")   # Ввод заголовка
print(f"username {title}")                   # После ввода переход к заголовку

content = input("Описание")                  # Ввод описания
status = input("Готовность задачи")          # Ввод готовности
print(f"content {status}")                   # После описания переход к задаче

created_date = input("Начало ДД.ММ.ГГ:")     # Ввод начала даты
issue_date = input("Завершение ДД.ММ.ГГ:")   # Ввод завершения даты
print(f"created_date {issue_date}")          # После ввода нач. даты переход к конечной даты
