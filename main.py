import numpy as np

a = 0
b = 0.1
n = 10
h = (b - a)/n
y_0 = 1

def f(x, y):
    return x + np.cos(y)

def euler():
    print("\n___ Метод Ейлера ___")

    derivative = y_0
    for i in range(n):
        derivative = derivative + f(h * i, derivative) * h
        print(f"Розраховане значенння y_{i + 1} = {derivative}")
    print("\nДля оцінки точності повторимо обчислення з кроком 2h")
    derivative_check = y_0
    for i in range(int(n / 2)):
        derivative_check = derivative_check + f((h * 2) * i, derivative_check) * (h * 2)
        print(f"Розраховане значенння y_{i + 1} = {derivative_check}")

    print(f"\nОцінка похибки, що досягає найбільшого значення в точці х = 0.1"
          f"\n∆ = {abs(derivative - derivative_check)}")

def modified_euler():
    print("\n___ Модифікований метод Ейлера ___")
    derivative = y_0
    for i in range(n):
        func_val = f(i * h, derivative)
        alfa_1 = f(i * h + h / 2, derivative + func_val * h / 2)
        print(f"Розраховане значенння a{i} = {alfa_1}")

        derivative = derivative + alfa_1 * h
        print(f"Розраховане значенння y_{i + 1} = {derivative}")

    print("\nДля оцінки точності повторимо обчислення з кроком 2h")
    derivative_check = y_0
    for i in range(int(n / 2)):
        func_val_check = f(i * h * 2, derivative_check)
        alfa_1_check = f(i * h * 2 + h, derivative_check + func_val_check * h)
        print(f"Розраховане значенння a{i} = {alfa_1_check}")

        derivative_check = derivative_check + alfa_1_check * (h * 2)
        print(f"Розраховане значенння y_{i + 1} = {derivative_check}")

    print(f"\nОцінка похибки, що досягає найбільшого значення в точці х = 0.1"
          f"\n∆ = {abs(derivative - derivative_check) / 3}")

def euler_cauchy():
    print("\n___ Метод Ейлера - Коші ___")
    derivative = y_0
    for i in range(n):
        alfa_1 = f(i * h, derivative)
        print(f"Розраховане значенння a1{i} = {alfa_1}")

        alfa_2 = f(i * h + h, derivative + alfa_1 * h)
        print(f"Розраховане значенння a2{i} = {alfa_2}")

        derivative = derivative + ((alfa_1 + alfa_2) / 2) * h
        print(f"Розраховане значення y_{i + 1} = {derivative}\n")

    print("\nДля оцінки точності повторимо обчислення з кроком 2h")
    derivative_check = y_0
    for i in range(int(n / 2)):
        alfa_1_check = f(i * h * 2, derivative_check)
        print(f"Розраховане значенння a1{i} = {alfa_1_check}")

        alfa_2_check = f(i * h * 2 + h * 2, derivative_check + alfa_1_check * (h * 2))
        print(f"Розраховане значенння a2{i} = {alfa_2_check}")

        derivative_check = derivative_check + ((alfa_1_check + alfa_2_check) / 2) * (h * 2)
        print(f"Розраховане значення y_{i + 1} = {derivative_check}\n")

    print(f"Оцінка похибки, що досягає найбільшого значення в точці х = 0.1"
          f"\n∆ = {abs(derivative - derivative_check) / 3}")

def runge_kuta():
    print("\n___ Метод Рунге - Кутта ___")
    derivative = y_0
    for i in range(n):
        k1 = f(i * h, derivative)
        k2 = f(i * h + h / 2, derivative + k1 * h / 2)
        k3 = f(i * h + h / 2, derivative + k2 * h / 2)
        k4 = f(i * h + h, derivative + k3 * h)

        print(f"Значення a1{i} = {k1}")
        print(f"Значення a2{i} = {k2}")
        print(f"Значення a3{i} = {k3}")
        print(f"Значення a4{i} = {k4}")

        derivative = derivative + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        print(f"Значення a{i} = {(1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)}")
        print(f"Обраховане значення y_{i + 1} = {derivative}\n")

    print("\nДля оцінки точності повторимо обчислення з кроком 2h")
    derivative_check = y_0
    for i in range(int(n / 2)):
        k1_check = f(i * h, derivative_check)
        k2_check = f(i * h + h / 2, derivative_check + k1_check * h / 2)
        k3_check = f(i * h + h / 2, derivative_check + k2_check * h / 2)
        k4_check = f(i * h + h, derivative_check + k3_check * h)

        print(f"Значення a1{i} = {k1_check}")
        print(f"Значення a2{i} = {k2_check}")
        print(f"Значення a3{i} = {k3_check}")
        print(f"Значення a4{i} = {k4_check}")

        derivative_check = derivative_check + (h / 6) * (k1_check + 2 * k2_check + 2 * k3_check + k4_check)
        print(f"Значення a{i} = {(1 / 6) * (k1_check + 2 * k2_check + 2 * k3_check + k4_check)}")
        print(f"Обраховане значення y_{i + 1} = {derivative_check}\n")

    print(f"Оцінка похибки, що досягає найбільшого значення в точці х = 0.1"
          f"\n∆ = {abs(derivative - derivative_check) / 15}")

def main():
    print("Комп'ютерний практикум №9 \nВаріант №11 \nВиконав студент групи ПБ-21 \nРозумняк Руслан\n")

    euler()
    modified_euler()
    euler_cauchy()
    runge_kuta()

if __name__ == "__main__":
    main()
