import time

def Greetings():
    print("Добро пожаловать в базу данных школьников!")
    
def HelpCmd():
    print("""\nСписок возможных команд для реализации:
        
/add: Добавить ученика в базу данных;
/clear: Очистить базу данных;
/cls: Очистить экран;
/delete: Удалить ученика из базы данных;
/exit: Выйти из программы;
/help: Вывести список возможных команд;
/list: Вывести список учеников;
/sort: Отобрать учеников по признакам.
""")

def ClearCmd():
    return input('\nВНИМАНИЕ! Эта команда удалит все из базы данных!\nДля подтверждения удаления наберите "да".\n')

def ClearedDB():
    print("\nТеперь база данных чиста, как попа младенца.\n")

def NotClearedDB():
    print("\nНичего не удалено.\n")

def ClsCmd():
    print("\nОчищаем экран:")

def BadMenuChoice():
    print("Значение введено неправильно.\nПожалуйста, попробуйте ещё раз.")

def ByeBye():
    print("\nЧто ж, надеюсь, увидимся снова...")
    time.sleep(1)

def StudentLastName():
    return input("\nПожалуйста, введите фамилию ученика: ")

def StudentFirstName():
    return input("Пожалуйста, введите имя ученика: ")

def StudentPatronymic():
    return input("Пожалуйста, введите отчество ученика: ")

def ClassNumber():
    while True:
        param = input("Пожалуйста, введите номер класса от 1 до 11: ")
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 1 and param <= 11: return param
                else: BadMenuChoice()
            except: BadMenuChoice()

def ClassLetter():
    return input("Пожалуйста, введите букву класса: ")

def RowNumber():
    while True:
        param = input("Пожалуйста, введите номер парты от 1 до 10: ")
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 1 and param <= 10: return param
                else: BadMenuChoice()
            except: BadMenuChoice()   

def DeskNumber():
    while True:
        param = input("Пожалуйста, введите номер ряда от 1 до 3: ")
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 1 and param <= 3: return param
                else: BadMenuChoice()
            except: BadMenuChoice()

def VariantNumber():
    while True:
        param = input("Пожалуйста, введите номер варианта от 1 до 2: ")
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 1 and param <= 2: return param
                else: BadMenuChoice()
            except: BadMenuChoice()

def GradeStatus():
    while True:
        param = input("""Пожалуйста, введите числом статус ученика из списка:

2: Двоечник;
3: Троечник;
4: Ударник;
5: Отличник.

""")
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 2 and param <= 5:
                    if param == 2: param = "двоечник"
                    elif param == 3: param = "троечник"
                    elif param == 4: param = "ударник"
                    elif param == 5: param = "отличник"
                    return param
                else: BadMenuChoice()
            except: BadMenuChoice()  

def IS():
    print("Введите команду:\n")
    return input("/")

def ItsClear():
    print("\nВ базе ничего нет :(\nМожет, стоит, что-то добавить через /add?")

def IdontKnow():
    print("""
Хмм... Похоже, я не знаю такую команду...

Что ж... Давайте попробуем снова...
""")

def NoData():
    print("Данных нет.")

def Complete():
    print("\nДанные заполнены.\n")

def YesOrNo():
    print('\nВведите "да" или "нет".')

def ListOut(array):
    for i in range(len(array)):
        print(f"Ученик {i + 1}:")
        print(f"""
Фамилия:        {array[i]["last_name"].capitalize()}
Имя:            {array[i]["first_name"].capitalize()}
Отчество:       {array[i]["patronymic"].capitalize()}
Класс:          {array[i]["class"]}
Буква класса:   {array[i]["letter"].capitalize()}
Ряд:            {array[i]["row"]}
Парта:          {array[i]["desk"]}
Вариант:        {array[i]["variant"]}
Статус:         {array[i]["grade_status"].capitalize()}\n""")

    time.sleep(0.5)

def AnyStudents():
    return input("Ещё будут ученики (да/нет)?\n")

def WriteAny(param):
    print(f"""Напишите часть или полное название параметра из списка, по которому хотите {param} данные:

1. Фамилия;
2. Имя;
3. Отчество;
4. Класс;
5. Буква класса;
6. Ряд;
7. Парта;
8. Вариант;
9. Статус.
""")
    while True:
        param = input()
        if param == "": return param
        else:
            try:
                param = int(param)
                if param >= 1 and param <= 9:
                    if param == 1: param = "last_name"
                    elif param == 2: param = "first_name"
                    elif param == 3: param = "patronymic"
                    elif param == 4: param = "class"
                    elif param == 5: param = "letter"
                    elif param == 6: param = "row"
                    elif param == 7: param = "desk"
                    elif param == 8: param = "variant"
                    elif param == 9: param = "grade_status"
                    return param
                else: BadMenuChoice()
            except: BadMenuChoice()

def Back():
    print("Возвращаемся...")

def EnterParamName(param):
    return input(f"\nНапишите часть или полное название параметра, с которым хотите {param} данные:\n")

def CheckList():
    print("\nЧто-то нет таких записей.\n\nПроверьте список через /list.")

def SomeData():
    print("\nПосмотрите, сколько таких записей я нашёл:\n")

def DataErased():
    print("\nДанные удалены.")

def SureToDelete():
    return input(f'Вы действительно хотите удалить эти данные (да/нет)?\n')

def EnterStudentNumber(arrayLength):
    while True:
        try:
            number = int(input("""Выберите номер ученика, данные которого хотите удалить.
Если желаете удалить все данные с совпадающим параметров, введите 0:\n"""))
            if number >= 0 and number <= arrayLength: return number 
            else: BadMenuChoice()
        except:
            BadMenuChoice()