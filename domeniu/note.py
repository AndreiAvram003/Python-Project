class Nota:
    def __init__(self, id_nota, student, disciplina, nota):
        self.__id_nota = id_nota
        self.__student = student
        self.__disciplina = disciplina
        self.__nota = nota

    def get_id_nota(self):
        return self.__id_nota

    def get_student(self):
        return self.__student

    def get_disciplina(self):
        return self.__disciplina

    def get_nota(self):
        return self.__nota

    def __str__(self):
        return f"Studentul {self.__student}, disciplina {self.__disciplina} si nota {self.__nota}"
