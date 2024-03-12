data = input("Введите нанные: ")

def fio_data(dataq):

    s = ""
    a = "".join(set(dataq))
    for i in a:
        if i.isalpha():
            s += i

    return s

def vremia_data(rvenia):
    
    s = 0

    a = "".join(set(rvenia))
    for i in a:
        if i.isalpha():
            s + i

    return s

    
result = fio_data(data)
resalt = vremia_data(data)
print(result)
print(len(result))
print(resalt)