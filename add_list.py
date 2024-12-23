title_1 = input("Введите перыый заголовок заметки: ")
title_2 = input("Введите второй заголовок заметки: ")
title_3 = input("Введите третий заголовок заметки: ")
titles = [title_1, title_2, title_3]
print(*titles, sep = ", ")
