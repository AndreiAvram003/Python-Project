import string
import random

from domeniu.student import Student


class ServiceStudenti:

    def __init__(self, validator_student, repo_studenti):
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti

    def adauga_student(self, id_student, nume):
        """

        :param id_student: id ul studentului care va fi adaugat
        :param nume: numele studentului care va fi adaugat
        :return:  studentul a fost adaugat
        """
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student)

    def get_all_studenti(self):
        """

        :return: preluarea tuturor studentilor din repo
        """
        return self.__repo_studenti.get_all()

    def sterge_student(self, id_student):
        """

        :param id_student: id-ul studentului care va fi sters
        :return:  lista cu disciplinele ramase
        """
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def modifica_student(self, id_student, nume_nou):
        """

        :param id_student: id ul care va fi modificat
        :param nume_nou: numele noului student
        :return:  studentul modificat cu succes
        """
        student_nou = Student(id_student, nume_nou)
        self.__validator_student.valideaza(student_nou)
        self.__repo_studenti.modifica_student(id_student, student_nou)
        
    def genereaza_random(self, n):
        """

        :param n: numarul de studenti doriti a fi generati
        :return: studentii au fost generati
        """
        while n > 0:
            try:
                id_random = random.randint(1, 1000 + self.__repo_studenti.get_size())
                nume_random = (''.join(random.choice(string.ascii_lowercase) for x in range(10)))
                student_random = Student(id_random, nume_random)
                self.__validator_student.valideaza(student_random)
                self.__repo_studenti.adauga_student(student_random)
            except ValueError:
                continue
            n = n - 1

    def ordoneaza_dupa_nume(self):
        """
         Ordoneaza studentii dupa numele lor string nume
        :return: lista cu studenti ordonati dupa nume
        """
        studenti = self.__repo_studenti.get_all()
        studenti_ordonati = sorted(studenti, key=lambda student: student.get_nume())
        return studenti_ordonati

    def ordoneaza_descrescator(self):
        """
         Ordoneaza studentii dupa numele lor string nume descrescator
        :return: lista cu studenti ordonati dupa nume descrescator
        """
        studenti = self.__repo_studenti.get_all()
        studenti_ordonati_descrescator = sorted(studenti, key=lambda student: student.get_nume(), reverse=True)
        return studenti_ordonati_descrescator
