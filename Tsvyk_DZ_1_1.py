# Домашнє завдання 2:
# На основі минулого домашнього завдання доробити скрипт таким чином, щоб запитувати у користувача інформацію про список справ. Приклад:
# Введіть дату: 01-01-2011.
# Введіть справу, яку необхідно не забути: помити посуд.
# Після цього на екран повинно бути виведено:
# Список справ на 01-01-2011:
# - сходити на тренування
# - помити посуд

dela_1 = {
    "2020-02-21": [
        {
        'AM-8': "Купить пиво ",
        'AM-10': "купить рыбки",
        'AM-12': "наслаждаться жизнью",
        },
        {
        'PM-14': "Продать рыбку",
        'PM-16': "продать пиво",
        'PM-18': "идти на завод"
        }
    ],
    "2020-02-22": [
        {
        'AM-8': "Пойти на работу",
        'AM-10': "написать код",
        'AM-12': "попить кофе",
        },
        {
        'PM-14': "Покушоть",
        'PM-16': "Пойти домой",
        'PM-18': "поспать"
        }
     ]
}
print(dela_1)
print(dela_1["2020-02-21"])
print(dela_1["2020-02-21"][0]['AM-8'])

# new_date = "2020-02-23"
# new_dela_2 = {
#     'AM-10': "Взять машину в аренду",
#     'PM-16': "Купить машину"
# }
# deal_list = [
#     new_dela_2,
# ]
#
# # привязываем список с делами по ключу даты
# dela_1[new_date] = deal_list
# print(dela_1['2020-02-23'])
#
# new_dela_3 = {
#     "AM-8": "Купить кикимару",
#     "AM-12": "Разжечь костёр",
#     "PM-14": "Сделать лук",
#     "PM-18": "Посадить лук"
# }
#
# dela_1[new_date].append(new_dela_3)
# dela_1[new_date].pop(0)
# dela_1.pop("2020-02-23")

