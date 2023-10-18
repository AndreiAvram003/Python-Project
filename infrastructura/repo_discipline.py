from erori.repo_error import RepoError


class RepoDiscipline:

    def __init__(self):
        self.__discipline = {}

    def adauga_disciplina(self, disciplina):
        """
         Adauga discipline in aplicatie impreuna cu id-ul, numele si profesorul lor
        :param disciplina: disciplina care va fi adaugata in aplicatie
        :return: disciplinele adaugate in aplicatie
        """
        if disciplina.get_id_disciplina() in self.__discipline:
            raise RepoError("Disciplina deja existenta!")
        else:
            self.__discipline[disciplina.get_id_disciplina()] = disciplina

    def sterge_disciplina_dupa_id(self, id_disciplina):
        """
         Se sterg studentii in functie de id-ul lor
        :param id_disciplina: id-ul disciplinei date spre stergere
        :return: lista cu disciplinele ramase dupa stergere
        """
        if id_disciplina not in self.__discipline:  # or self.__discipline[id_disciplina].sters()==True:
            raise RepoError("Disciplina inexistenta!")
        del self.__discipline[id_disciplina]  # .sterge()

    def cauta_disciplina_dupa_id(self, id_disciplina):
        if id_disciplina not in self.__discipline:
            raise RepoError("Disciplina inexistenta!")
        return self.__discipline[id_disciplina]

    def modifica_disciplina(self, id_disciplina, disciplina_noua):
        """
         Se modifica numele si profesorul disciplinei dorite
        :param id_disciplina: id-ul disciplinei date spre modificare
        :param disciplina_noua: numele nou si profesorul nou pentru disciplina modificata
        :return: disciplina modificate
        """
        if id_disciplina not in self.__discipline:
            raise RepoError("Disciplina inexistenta!")
        self.__discipline[id_disciplina] = disciplina_noua

    def get_all(self):
        discipline = []
        for disciplina_id in self.__discipline:
            discipline.append(self.__discipline[disciplina_id])
        return discipline

    def __len__(self):
        return len(self.__discipline)

    def get_size(self):
        return len(self.__discipline)
