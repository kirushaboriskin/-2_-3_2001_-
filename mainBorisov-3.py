def get_data(name):
    with open(name, "r") as f:
        text = f.read()
        data = text.split()
        f.close()
        try:
            numbers = list(map(int, data))
        except ValueError:
            print('Неверный ввод')
        else:
            return numbers


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


