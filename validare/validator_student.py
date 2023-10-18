from erori.validation_error import ValidError


class ValidatorStudent:

    def __init__(self):
        pass

    def valideaza(self, student):
        erori = ""
        if student.get_id_student() < 0:
            erori += "Id invalid!\n"
        if student.get_nume() == "":
            erori += "Nume invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)
