from erori.repo_error import RepoError


class RepoStudenti:

    def __init__(self):
        self.__studenti = {}

    def adauga_student(self, student):  # trebuie sa-mi asigure ca studentii mei sunt unic identificabili prin id-ul lor
        """
         Adauga studenti in aplicatie cu id-ul si numele lor
        :param student: studentul care va fi adaugat in aplicatie
        :return: lista cu studentii adaugati
        """
        id_student = student.get_id_student()
        if id_student in self.__studenti:
            raise RepoError("Student deja existent!")
        self.__studenti[id_student] = student

    def sterge_student_dupa_id(self, id_student):
        """
         Se sterge studentul dorit
        :param id_student: id-ul studentului care va fi sters
        :return: rezultat:lista care contine studentii ramasi dupa stergere
        """
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        del self.__studenti[id_student]

    def cauta_student_dupa_id(self, id_student):
        """
         Cauta un student dupa id-ul sau int id_student
        :param id_student: int
        :return: -
        """
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        return self.__studenti[id_student]

    def modifica_student(self, id_student, student):
        """
         Se modifica numele studentului dorit
        :param id_student: id-ul studentului dat spre modificare
        :param student: numele nou al studentului modificat
        :return: studentul modificat
        """
        if id_student not in self.__studenti:
            raise RepoError("Student inexistent!")
        self.__studenti[id_student] = student

    def get_all(self):
        """
         Returneaza lista tuturor studentilor
        :return: rezultat: lista de studenti
        """
        studenti = []
        for student_id in self.__studenti:
            studenti.append(self.__studenti[student_id])
        return studenti
        # sau return [x for x in self.__studenti.values()]

    def __len__(self):
        return len(self.__studenti)

    def get_size(self):
        """
          Returneaza lungimea listei de studenti
        :return: rezultat: lungimea listei de studenti
        """
        return len(self.__studenti)


""" 
from infrastructura.repo_studenti import RepoStudenti


class FileRepoStudenti(RepoStudenti):
    """"""
    Stocheaza/preia studentii din fisier
    """"""

    def __init__(self, calea_catre_fisier):
        RepoStudenti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            for line in lines:
                line = line.strip()
                if line != "":  # ca sa evitam sa avem o linie goala la sfarsit (face ce e mai departe doar daca linia curatata nu este linie goala)
                    parti = line.split(" ")
                    id_student = int(parti[0])
                    nume = parti[1]
                    student = Student(id_student, nume)
                    self._studenti[id_student] = student

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")

    def adauga_student(self, student):
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self, student)
        self.__write_all_to_file()

    def modifica_student(self, id_student, student):
        self.__read_all_from_file()
        RepoStudenti.modifica_student(self, id_student, student)
        self.__write_all_to_file()

    def sterge_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        RepoStudenti.sterge_student_dupa_id(self, id_student)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoStudenti.get_all(self)

    def cauta_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        return RepoStudenti.cauta_student_dupa_id(self, id_student)

    def get_size(self):
        self.__read_all_from_file()
        return RepoStudenti.get_size(self)
    """
