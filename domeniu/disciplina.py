class Disciplina:

    def __init__(self, id_disciplina, nume, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume = nume
        self.__profesor = profesor
        """self.__disciplina = {
                "id_disciplina": id_disciplina,
                "nume": nume,
                "profesor": profesor
        }"""
    """def creeaza_disciplina(self, id_disciplina, nume, profesor):
        """"""
         Creaza o disciplina cu id-ul de tip int id_disciplina, numele de tip string nume si profesorul de tip string profesor
        :param id_profesor: int
        :param nume: string
        :param profesor: string
        :return: disciplina cu id-ul id_disciplina, numele nume si profesorul profesor
        """"""
        self.__disciplina = {
            "id_disciplina": id_disciplina,
            "nume":nume,
            "profesor": profesor
        }
        return self.__disciplina
    """

    def get_id_disciplina(self):
        """
         Returneaza id-ul int id_disciplina al unei discipline
        :return: id-ul disciplinei
        """
        return self.__id_disciplina
    """return self.__disciplina["id_disciplina"]"""

    def get_nume(self):
        """
         Returneaza numele string nume al unei discipline
        :return: numele unei discipline
        """
        return self.__nume
    """return self.__disciplina["nume"]"""

    def set_nume(self, nume):
        """
         Modifica numele string nume al unei discipline
        :param nume: string
        :return: numele modificat al disciplinei
        """
        self.__nume = nume
    """self.__disciplina["nume"] = nume"""

    def get_profesor(self):
        """
         Returneaza profesorul string profesor al unei discipline
        :return: profesorul unei discipline
        """
        return self.__profesor
    """return self.__disciplina["profesor"]"""

    def set_profesor(self, profesor):
        """
         Modifica profesorul string profesor al unei discipline
        :param profesor: string
        :return: profesorul modificat al disciplinei
        """
        self.__profesor = profesor
    """self.__disciplina["profesor"] = profesor"""

    def __eq__(self, other):
        return self.__id_disciplina == other.__id_disciplina

    def __str__(self):
        return f"{self.__id_disciplina} {self.__nume} {self.__profesor}"
