def summarize(numbers):
    k = 0
    for elem in numbers:
        k += elem
    return k


def multiplication(numbers):
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result


def maximal(numbers):
    return sorted(numbers)[-1]


def minimal(numbers):
    return sorted(numbers)[0]


def is_valid(string):
    for i in string:
        if not i.isdigit():
            try:
                float(i)
                return True
            except ValueError:
                return False
    return True


file_name = input("Введите имя файла").strip()
f = open(file_name, 'r')
string = f.read().split(" ")
f.close()

if is_valid(string):
    numbers = list(map(float, string))
    print(f'Сумма всех чисел: {summarize(numbers)}')
    print(f'Произведение всех чисел: {multiplication(numbers)}')
    print(f'Максимальное число: {maximal(numbers)}')
    print(f'Минимальное число: {minimal(numbers)}')
else:
    print("Неверный формат ввода, числа в файле должны быть в одну строчку через пробел (разделитель - точка)")
