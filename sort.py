import UI
import time

def Sort(array):
    similiar = []
    param = UI.WriteAny("отсортировать")
    if param == "":
        UI.Back()
        time.sleep(0.5)
        return array
    choice = UI.EnterParamName("отсортировать")
    for i in range(len(array)):
        if str(choice).lower() in str((array[i][param])).lower():
            similiar.append(array[i])
    if similiar == []:
        UI.CheckList()
    else:
        UI.SomeData()
        UI.ListOut(similiar)