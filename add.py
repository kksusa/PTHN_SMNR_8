import UI

def AddCharacteristics(array):
    while True:
        dict = {"last_name": "", "first_name": "", "patronymic": "", "class": "", "letter": "", "row": "", "desk": "", "variant": "", "grade_status": ""}
        dict["last_name"] = UI.StudentLastName()
        dict["first_name"] = UI.StudentFirstName()
        dict["patronymic"] = UI.StudentPatronymic()
        dict["class"] = UI.ClassNumber()
        dict["letter"] = UI.ClassLetter()
        dict["row"] = UI.RowNumber()
        dict["desk"] = UI.DeskNumber()
        dict["variant"] = UI.VariantNumber()
        dict["grade_status"] = UI.GradeStatus()
        if dict["last_name"] == "" and dict["first_name"] == "" and dict["patronymic"] == "" and dict["class"] == "" and dict["letter"] == "" and dict["row"] == "" and dict["desk"] == "" and dict["variant"] == "" and dict["grade_status"] == "":
            UI.NoData()
        else:
            array.append(dict)
            UI.Complete()
        while True:
            answer = UI.AnyStudents()
            if answer.lower() == "да" or answer.lower() == "нет": break
            else:
                UI.YesOrNo()
                continue
        if answer.lower() == "нет":
            return array
            