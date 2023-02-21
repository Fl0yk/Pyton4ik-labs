def check_float(num):
    while not num.isdigit():
        num = input("Введите число, пожалуйста: ")
    return int(num)