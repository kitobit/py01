from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen

# Create your views here.
def index(request):
    data = {
        'title': 'Главная',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }

    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')

def sum(request):

    a = 5
    b = 6
    sum1 = a + b
    sum1 = 'Сумма 5 + 6 = ' + str(sum1)

    u = urlopen("http://python.org")  # открываем URL на чтение
    words = {}  # связываем имя words с пустым словарём
    # (словарь — неупорядоченный [[ассоциативный массив]])
    for line in u:  # читаем u по строкам
        line = line.decode("utf-8")  # преобразуем байт-строку в строку
        line = line.strip(" \n")  # отбрасываем начальные и конечные пробелы
        for word in line.split(" "):  # режем каждую строку на слова, ограниченные пробелами
            try:  # блок обработки исключений
                words[word] += 1  # пытаемся увеличить words[word] на единицу
            except KeyError:  # если не получилось (раньше words[word] не было)
                words[word] = 1  # присваиваем единицу

    # теперь словарь words содержит частоту встречаемости каждого слова.
    # Например, words может содержать {"яблоко":5, "апельсин": 12, "груша": 8}

    pairs = words.items()  # делаем из словаря список пар
    # pairs == [("яблоко",5), ("апельсин",12), ("груша",8)]
    A = sorted(pairs, key=lambda x: x[1], reverse=True)  # сортируем по убыванию второго элемента пары


    data = {
        'sum': sum1,
        'factorial': A[:10]
        }
    return render(request,'main/example.html',data)