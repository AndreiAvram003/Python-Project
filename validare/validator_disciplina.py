from erori.validation_error import ValidError


class ValidatorDisciplina:

    def __init__(self):
        pass

    def valideaza(self, disciplina):
        erori = ""
        if disciplina.get_id_disciplina() < 0:
            erori += "Id invalid!\n"
        if disciplina.get_nume() == "":
            erori += "Nume disciplina invalid!\n"
        if disciplina.get_profesor() == "":
            erori += "Profesor invalid!\n"
        if len(erori) > 0:
            raise ValidError(erori)
