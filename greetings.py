print("Hello, world!")

username = input("Имя пользователя:")
print(f"Привет, {username}!")                    # Делает приветствие и вовод имени пользователем

title = input("Заголовок заметки:")
content = input("Описание заметки:")
print(f"title, {content}")                       # Задаем заголовок и описание

status = input("Статус заметки")
created_date = input("Начало день-месяц-год")
issue_date = input("Конец день-месяц-год")
print(f"status, {created_date}, {issue_date}")    # Задем статус, дату начала и конец
