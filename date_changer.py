temp_created_date = "18-12-2024"
temp_issue_date = "22-12-2024"
remove_year = input("Скрыть год? (Да/Нет)")
if remove_year in ["Да","да"]:
    print(temp_created_date[:5:])
    print(temp_issue_date[:5:])
else:
        if remove_year in ["Нет","нет"]:
            print(temp_created_date)
            print(temp_issue_date)
        else:
                print("Некорректный ответ")