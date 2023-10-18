class Student:

    def __init__(self, id_student, nume):
        self.__id_student = id_student
        self.__nume = nume
        """self.__student = {
                "id_student": id_student,
                "nume": nume
        }

    def creeaza_student(self, id_student, nume):
        """"""
         Creaza un student cu id-ul de tip int id_student si numele de tip string nume
        :param id_student: int
        :param nume: string
        :return: studentul cu id-ul id_student si numele nume
        """"""
        self.__student = {
            "id_student": id_student,
            "nume": nume
        }
        return self.__student
        """

    def get_id_student(self):
        """
          Returneaza id-ul de tipul int id_student al unui student
        :return: id-ul unui student
        """
        return self.__id_student
        # return self.__student["id_student"]

    def get_nume(self):
        """
         Returneaza numele string nume al unui student
        :return: numele unui student
        """
        return self.__nume
        # return self.__student["nume"]

    def set_nume(self, nume):
        """
         Modificarea numele string nume al unui student
        :param nume: string
        :return: numele modificat al studentului
        """
        self.__nume = nume
        # self.__student["nume"] = nume

    def __eq__(self, other):  # eq suprascrie, verificam daca is egali studentii ca id
        return self.__id_student == other.__id_student

    def __str__(self):  # suprascriem str-ul care face un string si print-uieste
        return f"{self.__id_student} {self.__nume}"
