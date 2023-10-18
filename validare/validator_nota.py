from erori.validation_error import ValidError


class ValidatorNota:

    def __init__(self):
        pass

    def valideaza(self, nota):
        erori = ""
        if nota.get_id_nota() < 0:
            erori += "Id invalid!\n"
        e = 0.0000000001
        if nota.get_nota() < e:
            erori += "Nota invalida!\n"
        if len(erori) > 0:
            raise ValidError(erori)
