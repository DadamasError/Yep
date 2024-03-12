data = input("Введите нанные: ")

def fio_data(dataq):
    num_parts = 6 
    data = dataq.split()

    splitted_list = [data[i::6] for i in range(num_parts)]#Делим 

    summ = splitted_list[0:3]

    s = ""

    vihod = "".join(str(element) for element in summ)
    a = "".join(set(vihod))
    for i in a:
        if i.isalpha():
            s += i

    return s

def vremia_data(rvenia):
    num_parts = 6 

    splitted_list = [rvenia[i::6] for i in range(num_parts)]

    summ = splitted_list[3:]  # Изменяем диапазон, чтобы взять только цифры

    s = 0

    vihod = "".join(str(element) for element in summ)
    for i in vihod:
        if i.isdigit():
            s += int(i)
            return vihod

    
result = fio_data(data)
resalt = vremia_data(data)
print(result)
print(resalt)