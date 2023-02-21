def hello_world():
    print("Hello World!")


def doOperfirstNumtion(firstNum, secondNum, op):
    if op == "add":
        return firstNum+secondNum
    elif op == "sub":
        return firstNum-secondNum
    elif op == "mult":
        return firstNum*secondNum
    elif op == "div":
        if secondNum:
            return firstNum/secondNum
        return "Попытка деления на ноль"
    else:
        return "Такой функции нету"
