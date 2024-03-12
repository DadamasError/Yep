data = input("Введите нанные: ")

def process_data(data):
    


    n = 0

    for i in data:
        if isinstance(i, int):
            n += i
    return n
    



    num_parts = 6 

    splitted_list = [data[i::6] for i in range(num_parts)]

    vs = 0

    if isinstance(splitted_list[i], int):
        vs += i 

    summ = splitted_list[3:]  # Изменяем диапазон, чтобы взять только цифры

    s = ""

    vihod = "".join(str(element) for element in summ)
    a = ''.join(set(vihod))
    for i in a:
        if i.isdigit():  # Проверяем, является ли символ цифрой
            s += i

    return vs


result = process_data(data)
print(result)
