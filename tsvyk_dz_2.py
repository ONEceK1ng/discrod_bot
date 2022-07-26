print("Добрый день, Вас приветствует програма для организации дел на всю жизнь")

lifestream = {}

while True:
    answer = input("Желаете ввести новый продукт? (для выхода из программы введите 'stop'): ")
    if answer == "stop":
        print("Программа завершается...")
        break

    # получаем id нового продукта
    while True:
        product_id = input("Введите id нового продукта: ")
        if product_id in lifestream:
            print("Такой id уже есть в словаре! Введите другой!")
            continue
        break
  # запрашиваем название нового продукта
    while True:
        product_name = input("Введите название нового продукта: ")
        if product_name == "":
            print("Название продукта не может быть пустой строкой! Введите другое название!")
            continue
        break

    # запрашиваем производителя нового продукта
    while True:
        product_manufacturer = input("Введите производителя нового продукта: ")
        if product_manufacturer == "":
            print("Производитель продукта не может быть пустой строкой! Введите другого производителя!")
            continue
        break

    new_product = {
        "name": product_name,
        "manufacturer": product_manufacturer
    }
    lifestream[product_id] = new_product

    print("Новый продукт добавлен! Теперь список продуктов выглядит вот так:\n\n")
    for el in lifestream:
        print(el, ":", lifestream[el])

print("Программа завершена!")