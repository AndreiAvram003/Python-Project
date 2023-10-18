class NotaDTO:
    def __init__(self, id_nota, id_student, id_disciplina, nota):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__nota = nota

    def get_id_nota(self):
        return self.__id_nota

    def get_id_student(self):
        return self.__id_student

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_nota(self):
        return self.__nota

    def __str__(self):
        return f"{self.__id_nota} {self.__id_student} {self.__id_disciplina} {self.__nota}"
