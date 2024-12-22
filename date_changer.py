temp_created_date = "30.12.2024"
temp_issue_date = "31.12.2024"
remove_year = input('Скрыть год? Введите "да" или "нет"')
if remove_year.lower() == "да":
    print(temp_created_date[:5:])
    print(temp_issue_date[:5:])
else:
        if remove_year.lower() == "нет":
            print(temp_created_date)
            print(temp_issue_date)
        else:
                print("Некорректный ответ")
