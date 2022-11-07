import UI
import time

def Delete(array):
    similiar = []
    indicies = []
    param = UI.WriteAny("удалить")
    if param == "":
        UI.Back()
        time.sleep(0.5)
        return array
    choice = UI.EnterParamName("удалить")
    for i in range(len(array)):
        if str(choice).lower() in str((array[i][param])).lower():
            similiar.append(array[i])
            indicies.append(i)
    if similiar == []:
        UI.CheckList()
        return array
    else:
        UI.SomeData()
        UI.ListOut(similiar)
        number = UI.EnterStudentNumber(len(similiar))
        while True:
            answer = UI.SureToDelete()
            if answer.lower() == "да":
                if number > 0:
                    array.pop(indicies[number - 1])
                else:
                    for i in range(len(indicies) - 1, -1, -1): array.pop(indicies[i])
                UI.DataErased()
                return array
            elif answer.lower() == "нет":
                UI.NotClearedDB()
                return array
            else: UI.YesOrNo()