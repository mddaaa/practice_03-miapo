def divide(a, b):
    if b == 0:
        return "На ноль делить нельзя"
    return a / b

if __name__ == "__main__":
    print("1. Деление")
    choice = input("Выбери: ")
    if choice == "1":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Ответ: {divide(x, y)}")