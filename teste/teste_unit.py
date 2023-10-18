import unittest

from domeniu.disciplina import Disciplina
from domeniu.note import Nota
from domeniu.student import Student
from infrastructura.repo_studenti import RepoStudenti
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from validare.validator_disciplina import ValidatorDisciplina
from validare.validator_student import ValidatorStudent


class Teste(unittest.TestCase):
    def setUp(self):
        self.__id_student = 5
        self.__nume_student = "Vasile"
        self.__student=Student(self.__id_student,self.__nume_student)

        self.__id_disciplina = 24
        self.__nume_disciplina = "Analiza"
        self.__profesor ="Berinde"
        self.__disciplina  = Disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)

        self.__id_student_nou = 6
        self.__nume_student_nou = "Ion"
        self.__student_nou =Student(self.__id_student_nou,self.__nume_student_nou)

        self.__id_nota = 1
        self.__valoare_nota = 7
        self.__nota = Nota(self.__id_nota,self.__student,self.__disciplina,self.__valoare_nota)

    def ruleaza_teste_domain(self):
        self.assertTrue(self.__disciplina.get_id_disciplina() == self.__id_disciplina)
        self.assertTrue(self.__disciplina.get_nume() == self.__nume_disciplina)
        self.assertTrue(self.__disciplina.get_profesor() == self.__profesor)
        self.assertTrue(self.__student.get_id_student() == self.__id_student)
        self.assertTrue(self.__student.get_nume()== self.__nume_student)
        self.assertTrue(self.__nota.get_id_nota()==self.__id_nota)
        self.assertTrue(self.__nota.get_student() == self.__student)

    def ruleaza_teste_validare(self):
        self.__validator_student = ValidatorStudent()
        self.__validator_student.valideaza(self.__student)

        self.__id_invalid_student = -5
        self.__nume_invalid_student = ""
        self.__student_invalid = Student(self.__id_invalid_student, self.__nume_invalid_student)

        self.assertRaises(ValidError,self.__validator_student.valideaza, self.__student_invalid)

        self.__validator_disciplina = ValidatorDisciplina()
        self.__validator_disciplina.valideaza(self.__disciplina)

        self.__id_invalid_disciplina = -5
        self.__nume_invalid_disciplina = ""
        self.__profesor_invalid=""
        self.__disciplina_invalida = Disciplina(self.__id_invalid_disciplina, self.__nume_invalid_disciplina,self.__profesor_invalid)
        self.assertRaises(ValidError,self.__validator_disciplina.valideaza,self.__disciplina_invalida)

    def ruleaza_teste_repo_student(self):
        self.__repo_student = RepoStudent()
        self.assertTrue(len(self.__repo_student) == 0)
        self.__student = Student(self.__id_student, self.__nume_student)
        self.__repo_student.adauga_student(self.__student)
        self.assertTrue(len(self.__repo_student) == 1)

        self.assertRaises(RepoError, self.__repo_student.adauga_student,self.__student)

        self.assertTrue(self.__repo_student.cauta_student_dupa_id(self.__id_student) == self.__student)
        self.__id_inexistent = 35236
        self.assertRaises(RepoError,self.__repo_student.cauta_student_dupa_id,self.__id_inexistent)

        self.__id_student_nou = 125
        self.__nume_student_nou = "Costel"
        self.__student_nou = Student(self.__id_student_nou, self.__nume_student_nou)
        self.__repo_student.adauga_student(self.__student_nou)
        self.assertTrue(len(self.__repo_student) == 2)
        self.__repo_student.sterge_student_dupa_id(self.__student_nou.get_id_student())
        self.assertTrue(len(self.__repo_student) == 1)

        self.assertRaises(RepoError,self.__repo_student.sterge_student_dupa_id,self.__id_inexistent)

        self.__student_modificat = Student(self.__id_student,self.__nume_student_nou)
        self.__repo_student.modifica_student(self.__id_student,self.__student_modificat)
        self.assertTrue(len(self.__repo_student) == 1)

        self.assertRaises(RepoError,self.__repo_student.modifica_student,self.__id_inexistent,Student(self.__id_inexistent,None))

        studenti = self.__repo_student.get_all()
        self.assertTrue(len(studenti) == 1)
        self.assertTrue(studenti[0] == self.__student_modificat)
