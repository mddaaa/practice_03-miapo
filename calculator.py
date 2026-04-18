def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print("1. Умножение")
    choice = input("Выбери: ")
    if choice == "1":
        x = float(input("Число 1: "))
        y = float(input("Число 2: "))
        print(f"Ответ: {multiply(x, y)}")