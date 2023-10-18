from erori.repo_error import RepoError


class RepoNote:

    def __init__(self):
        self.__note = {}

    def adauga_nota(self, nota):
        """

        :param nota: nota care va fi adaugata
        :return: nota a fost adaugata
        """
        nota_id = nota.get_id_nota()
        if nota_id in self.__note:
            raise RepoError("Nota deja existenta!")
        self.__note[nota_id] = nota

    def sterge_nota_dupa_id(self, id_nota):
        """

        :param id_nota: id ul notei care va fi stearsa
        :return: nota a fost stearsa
        """
        if id_nota not in self.__note:
            raise RepoError("Nota inexistenta!")
        del self.__note[id_nota]

    def get_all(self):
        """

        :return: totalitatea notelor
        """
        note = []
        for nota_id in self.__note:
            note.append(self.__note[nota_id])
        return note

    def __len__(self):
        return len(self.__note)
