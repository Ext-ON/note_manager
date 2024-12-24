note = []
username = input("Имя пользователя: ")
title = input("Заголовок заметки: ")
content = input("Описание заметки: ")
status = input("Статус заметки:")
created_data = input('Дата создания заметки в формате "01.01.2024": ')
issue_data = input('Дата истечения заметки(дедлайн) в фориате "01.01.2024": ')

title_1 = input("Введите первый подзаголовок заметки: ")
title_2 = input("Введите второй подзаголовок зпметки: ")
titles = [title_1, title_2]

note = [username, title, content, 
        status, created_data, issue_data]
note.append(titles)
print(*note, sep = "\n")
