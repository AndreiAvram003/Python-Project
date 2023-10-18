class Primii20:

    def __init__(self, student, medie_student):
        self.__student = student
        self.__medie_student = medie_student

    def get_student(self):
        return self.__student

    def get_medie(self):
        return self.__medie_student

    def __str__(self):
        return f"Studentul {self.__student} cu media {self.__medie_student}"

    def __lt__(self, other):
        return self.__medie_student < other.__medie_student
