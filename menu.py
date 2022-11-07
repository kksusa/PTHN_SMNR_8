from os import system
from time import sleep
import UI
import dataManage
import add
import sort
import delete

def Action():
    system('clear')
    array = dataManage.ReadData()
    UI.Greetings()
    UI.HelpCmd()
    while True:
        cmd = UI.IS()
        if cmd == "help":
            UI.HelpCmd()
        elif cmd == "add":
            add.AddCharacteristics(array)
            dataManage.SaveData(array)
        elif cmd == "clear":
            answer = UI.ClearCmd()
            if answer.lower() == "да":
                array = []
                dataManage.SaveData(array)
                UI.ClearedDB()
            else: UI.NotClearedDB()
        elif cmd == "cls":
            UI.ClsCmd()
            for i in range(3, 0, -1):
                print(i)
                sleep(1)
            system('clear')
        elif cmd == "sort":
            if array != []: sort.Sort(array)
            else: UI.ItsClear()
        elif cmd == "delete":
            if array != []: delete.Delete(array)
            else: UI.ItsClear()
            dataManage.SaveData(array)
        elif cmd == "exit":
            UI.ByeBye()
            break
        elif cmd == "list":
            if array != []: UI.ListOut(array)
            else: UI.ItsClear()
        else: UI.IdontKnow()