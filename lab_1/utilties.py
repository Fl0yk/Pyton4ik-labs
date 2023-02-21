def check_integer(num):
    while not num.isdigit():
        num = input("Введите число, пожалуйста: ")
    return int(num)


def check_list(listNum):
    for num in listNum:
        if not num.isdigit():
            return []
    return [int(num) for num in listNum]