import pickle
import re
import math
from itertools import accumulate
from functools import partial

# Задача № 1
# Задание № 1 Формирование словаря с требуемыми пар-ми
"""Лира двигалась вместе с людьми, а мать крепко сжимала ее тонкую руку. Толпа была чудовищем, монстром с миллионом орущих ртов и бесчисленными глазами,
 в которых сверкало пламя, и Лира знала, если она упадет, то умрет, раздавленная безразличными ногами, однако это не имело для нее значения.
"""
# подсчет слов в каждом предложении
def wordsInASentence(someText):
    wordsList = []
    strBuf = someText + " "
    try:
        for i in range(len(someText.split(". "))):
            indexBuf = strBuf.index(".") + 1 # индекс конца первого предложения
            strBuf = strBuf[:indexBuf] # предложение до первой точки
            wordsList.append(f"Предложение {i + 1}: {len(strBuf.split())}") # количество слов в предложении с пробелами
            strBuf = someText[indexBuf:] # обрезаем обработанное предложение
    except:
        print("Что-то не так с полученным текстом")
    return wordsList

# подсчет букв в словах
def lettersInWords(someText):
    resDict = {}
    try:
        someText = someText.replace(".", "") # удаление лишних символов, можно учесть еще какие-то по необходимости
        someText = someText.replace(",", "")
        someText = someText.replace("-", "")
        dict = someText.split()
        for i in dict:
            resDict[i] = len(i)
    except:
        print("Что-то не так с полученным текстом")
    return resDict

# подсчет пунктуации в тексте
def punctuation(someText):
    try:
        resDict = {'.' : someText.count('.'),
                   ',' : someText.count(','),
                   '-' : someText.count('-')}
    except:
        print("Что-то не так с полученным текстом")
    return resDict

# работа с файлом
with open("text.txt", mode="r", encoding="utf-8") as file:
    try:
        file = file.read() # сохраняем текст из файла в строку
        sentences = re.sub("([\.]) ", "\\1\n", file).split("\n") # сохраняем предложения в список
        infoDict = {'Всего слов' : len(file.split()),
                    'Количество предложений' : file.count("."),
                    'Количество слов в предложениях' : wordsInASentence(file),
                    'Количество букв в словах' : lettersInWords(file),
                    'Знаки препинания' : punctuation(file)}
    except:
        print("Не удалось подключиться к файлу")


# Задание № 2 Сохранение полученного словаря в двоичный файл, загрузка сохраненного словаря
with open("text1.bin", "wb") as file1: # сохраняем данные в двоичный файл
    try:
        pickle.dump(infoDict, file1)
    except:
        print("Не удалось сохранить файл")

with open("text1.bin", "rb") as file1: # загружаем данные из двоичного файла
    try:
        infoDictRestored = pickle.load(file1)
    except:
        print("Не удалось загрузить файл")


# Задание № 3 Вывод информации из словаря
print(f"Текст содержит {infoDictRestored['Всего слов']} слов и {infoDictRestored['Количество предложений']} предложения")
for i in infoDictRestored['Количество слов в предложениях']:
    print(i)
for key, value in infoDictRestored['Количество букв в словах'].items():
    print(f"\tБукв в слове {key}: {value}")
print("Знаки препинания:")
for key, value in infoDictRestored['Знаки препинания'].items():
    print(f"\t'{key}': {value}")


# Задание № 4 Ввод количества предложений в абзацах и их формирование
while True:
    try:
        n = int(input("\nПожалуйста, введите n (количество предложений в абзаце): "))
        if n != 0:
            break
    except:
        print("Вы допустили ошибку при вводе n, пожалуйста, повторите ввод")

# Разбиваем текст на абзацы из n предложений
paragraphs = [[]]

for sentence in sentences:
    if len(paragraphs[-1]) < n:
        paragraphs[-1].append(sentence)
    else:
        paragraphs.append([sentence])


# Задание № 5 Сортировка абзацев по возрастанию количества слов в них
try:
    paragraphs.sort(key=lambda paragraph: len([word for sentence in paragraph for word in sentence.split()]))
except:
    print("Сортировка абзацев не удалась")


# Задание № 6 Сохранение полученных данных в новый файл
# формирование текста для сохранения в файл
text = ""
for paragraph in paragraphs:
    text += "\n".join(paragraph)
print(text)

with open("text2.txt", mode="w") as file:
    try:
        file.write(text)
    except:
        print("Не удалось записать данные в файл")


# Задача № 2
"""
Инвест. проект заключается в том, что необходимо построить пустынную трассу и полигон для создания машин, чтобы
устраивать гонки на выживание для всех желающих с трансляцией для зрителей по всему миру.
Первоначальные затраты: 15 млн долларов на оборудование пустынной трассы смертельными ловушками, постройку полигона для
создания машин, закупку необходимых материалов для постройки машин, обучение персонала и рекламную компанию.
Регулярный доход: 4.99 млн долларов от продажи билетов и заработока с рекламы.
Регулярный расход: 2 млн долларов на закупку нового оборудования, очистку пустыни, зарплату персоналу, постоянную
рекламную компанию и урегулирования проблем с властями.
Срок реализации проекта: 7 лет.
Ставка дисконтирования: 9%.
"""

def calcNPV(firstCost, income, cost, implTime, disRate):
    """Функция вычисляет NPV и DPP проекта"""
    try:
        NPVlist = [-firstCost] + [(income - cost) / (1 + disRate) ** i for i in range(1, implTime + 1)]
        NPVaccum = list(accumulate(NPVlist))
        NPV = NPVaccum[-1] # чистая приведенная стоимость проекта
        m = len([npvacc for npvacc in NPVaccum if npvacc < 0]) - 1
        DPP = m + abs(NPVaccum[m]) / NPVlist[m + 1] if len(NPVlist) > m + 1 else None # cрок окупаемости проекта
    except:
        print("Некорректные входные данные")
    return NPV, DPP


# входные данные
firstCost = 15 # Первоначальные затраты
income = 4.99 # Регулярный доход
cost = 2 # Регулярный расход
implTime = 7 # Срок реализации проекта
disRate = 0.09 # Ставка дисконтирования

# считаем NPV, DPP
NPV, DPP = calcNPV(firstCost, income, cost, implTime, disRate)

# считаем внутреннюю форму дохоности (IRR)
try:
    calcNPV0 = partial(calcNPV, firstCost=firstCost, income=income, cost=cost, implTime=implTime)
    minNPV, IRR = math.inf, None
    for disRate in range(1, 101):
        NPVirr = calcNPV0(disRate=disRate / 100)[0]
        if abs(NPVirr) < abs(minNPV):
            minNPV, IRR = NPVirr, disRate / 100

    if IRR <= 0.02 or IRR >= 0.99:
        print("IRR проекта с текущими параметрами отсутствует"
              "выбран узкий диапазон изменения ставки дисконтирования")
        IRR = None
except:
    print("Некорректные входные данные")

print("\nРасчет финансовых показателей инвестиционного проекта.")
print(f"NPV = {NPV}, DPP = {DPP}, IRR = {IRR}: проект {'' if NPV > 0 else 'не'}эффективен")
