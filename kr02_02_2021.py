def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """
s = []
for i in two_dim_words:
    s += i
s.sort(key=len)
print(s)
    return s


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """
s = {}
n = []
n2 = []
h = set(numbers)
for i in range(9):
    n.append(numbers.count(i))
for i in range(4):
    n2.append(max(n))
    f = n.index(max(n))
    s[f] = max(n)
    n.pop(f)

    return s


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return pass


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return pass


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return pass


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
n = set()
mm = []
r = (len(lsy1), len(lst2))
k = int(max(r))
j = int(min(r))
n = set(lst1)
g = set(lst2)
l = n - g
mm = list(l)
mm.sort()

    return mm


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """

    return pass

