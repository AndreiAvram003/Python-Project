from domeniu.student import Student
from erori.repo_error import RepoError


class FileRepoStudenti:
    """
    Stocheaza/preia studentii din fisier
    """

    def __init__(self, calea_catre_fisier):
        self.__studenti = {}
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        """
        Se citeste intreg continutul fisierului
        :return: -
        """
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self.__studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":  # ca sa evitam sa avem o linie goala la sfarsit (face ce e mai departe doar daca linia curatata nu este linie goala)
                    parti = line.split(" ")
                    id_student = int(parti[0])
                    nume = parti[1]
                    student = Student(id_student, nume)
                    self.__studenti[id_student] = student

    def __write_all_to_file(self):
        """
        Se stocheaza studentii in fisier
        :return: -
        """
        with open(self.__calea_catre_fisier, "w") as f:
            for student in self.__studenti.values():
                f.write(str(student)+"\n")

    def adauga_student(self, student):
        """
         Adauga studenti in aplicatie cu id-ul si numele lor
        :param student: studentul care va fi adaugat in aplicatie
        :return: lista cu studentii adaugati
        """
        self.__read_all_from_file()
        id_student = student.get_id_student()
        if id_student in self.__studenti:
            raise RepoError("Student deja existent!")
        self.__studenti[id_student] = student
        self.__write_all_to_file()

    def modifica_student(self, id_student, student):
        """
         Se modifica numele studentului dorit
        :param id_student: id-ul studentului dat spre modificare
        :param student: numele nou al studentului modificat
        :return: studentul modificat
        """
        self.__read_all_from_file()
        id_student = student.get_id_student()
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        self.__studenti[id_student] = student
        self.__write_all_to_file()

    def sterge_student_dupa_id(self, id_student):
        """
         Se sterge studentul dorit
        :param id_student: id-ul studentului care va fi sters
        :return: rezultat: lista care contine studentii ramasi dupa stergere
        """
        self.__read_all_from_file()
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        del self.__studenti[id_student]
        self.__write_all_to_file()

    def cauta_student_dupa_id(self, id_student):
        """
         Cauta un student dupa is-ul sau int id_student
        :param id_student: int
        :return: -
        """
        self.__read_all_from_file()
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        return self.__studenti[id_student]

    def get_all(self):
        """
         Returneaza lista tuturor studentilor
        :return: lista tuturor studentilor
        """
        self.__read_all_from_file()
        studenti = []
        for student_id in self.__studenti:
            studenti.append(self.__studenti[student_id])
        return studenti

    def __len__(self):
        return len(self.__studenti)

    def get_size(self):
        """
         Returneaza lungimea listei cu studenti
        :return: rezultat: int - lungimea listei cu studenti
        """
        self.__read_all_from_file()
        return len(self.__studenti)
