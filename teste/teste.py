from domeniu.note import Nota
# from infrastructura.repo_note import RepoNote
from validare.validator_disciplina import ValidatorDisciplina
# from validare.validator_nota import ValidatorNota
from validare.validator_student import ValidatorStudent
from domeniu.disciplina import Disciplina
from domeniu.student import Student
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from infrastructura.repo_studenti import RepoStudenti
from infrastructura.repo_discipline import RepoDiscipline
from business.service_discipline import ServiceDiscipline
from business.service_studenti import ServiceStudenti
# from business.service_note import ServiceNote


class Teste(object):
    def __init__(self):
        self.__id_student = 1
        self.__nume_student = "Marian"
        self.__student = Student(self.__id_student, self.__nume_student)

        self.__id_disciplina = 2
        self.__nume_disciplina = "Analiza"
        self.__profesor = "Berinde"
        self.__disciplina = Disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)

        self.__id_student_nou = 1
        self.__nume_student_nou = "David"
        self.__student_nou = Student(self.__id_student_nou, self.__nume_student_nou)

        self.__id_nota = 1
        self.__valoare_nota = 7
        self.__nota = Nota(self.__id_nota, self.__student, self.__disciplina, self.__valoare_nota)

    def __ruleaza_teste_domeniu(self):
        assert(self.__disciplina.get_id_disciplina() == self.__id_disciplina)
        assert(self.__disciplina.get_nume() == self.__nume_disciplina)
        assert(self.__disciplina.get_profesor() == self.__profesor)
        assert(self.__student.get_id_student() == self.__id_student)
        assert(self.__student.get_nume() == self.__nume_student)
        assert(self.__nota.get_id_nota() == self.__id_nota)
        assert(self.__nota.get_student() == self.__student)

    def __ruleaza_teste_validare(self):
        self.__validator_student = ValidatorStudent()
        self.__validator_student.valideaza(self.__student)

        self.__id_invalid_student = -5
        self.__nume_invalid_student = ""
        self.__student_invalid = Student(self.__id_invalid_student, self.__nume_invalid_student)
        try:
            self.__validator_student.valideaza(self.__student_invalid)
            assert False
        except ValidError as ve:
            assert(str(ve) == "Id invalid!\nNume invalid!\n")

        self.__validator_disciplina = ValidatorDisciplina()
        self.__validator_disciplina.valideaza(self.__disciplina)

        self.__id_invalid_disciplina = -5
        self.__nume_invalid_disciplina = ""
        self.__profesor_invalid = ""
        self.__disciplina_invalida = Disciplina(self.__id_invalid_disciplina, self.__nume_invalid_disciplina, self.__profesor_invalid)
        try:
            self.__validator_disciplina.valideaza(self.__disciplina_invalida)
            assert False
        except ValidError as ve:
            assert(str(ve) == "Id invalid!\nNume disciplina invalid!\nProfesor invalid!\n")

    def __ruleaza_teste_repo_studenti(self):
        self.__repo_studenti = RepoStudenti()
        assert(len(self.__repo_studenti) == 0)
        self.__student = Student(self.__id_student, self.__nume_student)
        self.__repo_studenti.adauga_student(self.__student)
        assert(len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.adauga_student(self.__student)
            assert False
        except RepoError as re:
            assert(str(re) == "Student deja existent!")

        assert(self.__repo_studenti.cauta_student_dupa_id(self.__id_student) == self.__student)
        self.__id_inexistent = 35236
        try:
            self.__repo_studenti.cauta_student_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        self.__id_student_nou = 125
        self.__nume_student_nou = "Costel"
        self.__student_nou = Student(self.__id_student_nou, self.__nume_student_nou)
        self.__repo_studenti.adauga_student(self.__student_nou)
        assert(len(self.__repo_studenti) == 2)
        self.__repo_studenti.sterge_student_dupa_id(self.__student_nou.get_id_student())
        assert(len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.sterge_student_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        self.__student_modificat = Student(self.__id_student, self.__nume_student_nou)
        self.__repo_studenti.modifica_student(self.__id_student, self.__student_modificat)
        assert(len(self.__repo_studenti) == 1)
        try:
            self.__repo_studenti.modifica_student(self.__id_inexistent, Student(self.__id_inexistent, None))
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        studenti = self.__repo_studenti.get_all()
        assert(len(studenti) == 1)
        assert(studenti[0] == self.__student_modificat)

    def __ruleaza_teste_repo_discipline(self):

        self.__repo_discipline = RepoDiscipline()
        assert(len(self.__repo_discipline) == 0)
        self.__disciplina = Disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)
        self.__repo_discipline.adauga_disciplina(self.__disciplina)
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.adauga_disciplina(self.__disciplina)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina deja existenta!")

        assert(self.__repo_discipline.cauta_disciplina_dupa_id(self.__id_disciplina) == self.__disciplina)
        self.__id_inexistent = 35236
        try:
            self.__repo_discipline.cauta_disciplina_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta!")

        self.__id_disciplina_noua = 125
        self.__nume_disciplina_noua = "Haha"
        self.__profesor_nou = "Ion"
        self.__disciplina_noua = Disciplina(self.__id_disciplina_noua, self.__nume_disciplina_noua, self.__profesor_nou)
        self.__repo_discipline.adauga_disciplina(self.__disciplina_noua)
        assert(len(self.__repo_discipline) == 2)
        self.__repo_discipline.sterge_disciplina_dupa_id(self.__disciplina_noua.get_id_disciplina())
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.sterge_disciplina_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta!")

        self.__disciplina_modificata = Disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor_nou)
        self.__repo_discipline.modifica_disciplina(self.__id_disciplina, self.__disciplina_modificata)
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.modifica_disciplina(self.__id_inexistent, Disciplina(self.__id_inexistent, None, None))
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta!")

        discipline = self.__repo_discipline.get_all()
        assert(len(discipline) == 1)
        assert(discipline[0] == self.__disciplina_modificata)

    def __ruleaza_teste_service_studenti(self):
        self.__repo_studenti = RepoStudenti()
        self.__service_studenti = ServiceStudenti(self.__validator_student, self.__repo_studenti)
        assert (len(self.__repo_studenti) == 0)
        self.__service_studenti.adauga_student(self.__id_student, self.__nume_student)
        assert (len(self.__repo_studenti) == 1)

        studenti = self.__service_studenti.get_all_studenti()
        assert (len(studenti) == 1)
        assert (studenti[0] == self.__student)
        self.__student_modificat = Student(self.__id_student, self.__nume_student_nou)
        self.__service_studenti.modifica_student(self.__id_student, self.__nume_student_nou)
        assert(studenti[0] == self.__student_modificat)

        assert (len(self.__repo_studenti) == 1)
        self.__service_studenti.sterge_student(self.__id_student)
        assert (len(self.__repo_studenti) == 0)

    def __ruleaza_teste_service_discipline(self):
        self.__repo_discipline = RepoDiscipline()
        self.__service_discipline = ServiceDiscipline(self.__validator_disciplina, self.__repo_discipline)
        assert (len(self.__repo_discipline) == 0)
        self.__service_discipline.adauga_disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)
        assert (len(self.__repo_discipline) == 1)
        discipline = self.__service_discipline.get_all_discipline()
        assert (len(discipline) == 1)
        assert (discipline[0] == self.__disciplina)
        self.__disciplina_modificata = Disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor)
        self.__service_discipline.modifica_disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor_nou)
        assert(discipline[0] == self.__disciplina_modificata)

        assert (len(self.__repo_discipline) == 1)
        self.__service_discipline.sterge_disciplina(self.__id_disciplina)
        assert (len(self.__repo_discipline) == 0)

    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo_studenti()
        self.__ruleaza_teste_repo_discipline()

        self.__ruleaza_teste_service_studenti()
        self.__ruleaza_teste_service_discipline()


"""
class Teste(object):

    def __init__(self):
        self.__id_student = 5
        self.__nume_student = "Vasile"
        self.__student = Student(self.__id_student, self.__nume_student)

        self.__id_disciplina = 24
        self.__nume_disciplina = "Analiza"
        self.__profesor = "Berinde"
        self.__disciplina = Disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)

        self.__id_student_nou = 6
        self.__nume_student_nou = "Ion"
        self.__student_nou = Student(self.__id_student_nou, self.__nume_student_nou)

        self.__id_nota = 1
        self.__valoare_nota = 7
        self.__nota = Nota(self.__id_nota, self.__student, self.__disciplina, self.__valoare_nota)

    def ruleaza_toate_testele(self):
        self.__ruleaza_teste_domain()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo_student()
        self.__ruleaza_teste_repo_disciplina()
        self.__ruleaza_teste_service_studenti()
        self.__ruleaza_teste_service_disciplline()
        self.__ruleaza_teste_repo_note()
        self.__ruleaza_teste_service_note()
        self.__blackboxtesting()

    def __ruleaza_teste_domain(self):
        assert(self.__disciplina.get_id_disciplina() == self.__id_disciplina)
        assert(self.__disciplina.get_nume() == self.__nume_disciplina)
        assert(self.__disciplina.get_profesor() == self.__profesor)
        assert(self.__student.get_id_student() == self.__id_student)
        assert(self.__student.get_nume() == self.__nume_student)
        assert(self.__nota.get_id_nota() == self.__id_nota)
        assert(self.__nota.get_student() == self.__student)

    def __ruleaza_teste_validare(self):
        self.__validator_student = ValidatorStudent()
        self.__validator_student.valideaza(self.__student)

        self.__id_invalid_student = -5
        self.__nume_invalid_student = ""
        self.__student_invalid = Student(self.__id_invalid_student, self.__nume_invalid_student)
        try:
            self.__validator_student.valideaza(self.__student_invalid)
            assert False
        except ValidError as ve:
            assert(str(ve) == "Id invalid!\nNume invalid!\n")

        self.__validator_disciplina = ValidatorDisciplina()
        self.__validator_disciplina.valideaza(self.__disciplina)

        self.__id_invalid_disciplina = -5
        self.__nume_invalid_disciplina = ""
        self.__profesor_invalid = ""
        self.__disciplina_invalida = Disciplina(self.__id_invalid_disciplina, self.__nume_invalid_disciplina, self.__profesor_invalid)
        try:
            self.__validator_disciplina.valideaza(self.__disciplina_invalida)
            assert False
        except ValidError as ve:
            assert(str(ve) == "Id_disciplina invalid!\nNume invalid!\nProfesor invalid!\n")

    def __ruleaza_teste_repo_student(self):
        self.__repo_student = RepoStudenti()
        assert(len(self.__repo_student) == 0)
        self.__student = Student(self.__id_student, self.__nume_student)
        self.__repo_student.adauga_student(self.__student)
        assert(len(self.__repo_student) == 1)
        try:
            self.__repo_student.adauga_student(self.__student)
            assert False
        except RepoError as re:
            assert(str(re) == "Student existent!")

        assert(self.__repo_student.cauta_student_dupa_id(self.__id_student) == self.__student)
        self.__id_inexistent = 35236
        try:
            self.__repo_student.cauta_student_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        self.__id_student_nou = 125
        self.__nume_student_nou = "Costel"
        self.__student_nou = Student(self.__id_student_nou, self.__nume_student_nou)
        self.__repo_student.adauga_student(self.__student_nou)
        assert(len(self.__repo_student) == 2)
        self.__repo_student.sterge_student_dupa_id(self.__student_nou.get_id_student())
        assert(len(self.__repo_student) == 1)
        try:
            self.__repo_student.sterge_student_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        self.__student_modificat = Student(self.__id_student, self.__nume_student_nou)
        self.__repo_student.modifica_student(self.__id_student, self.__student_modificat)
        assert(len(self.__repo_student) == 1)
        try:
            self.__repo_student.modifica_student(self.__id_inexistent, Student(self.__id_inexistent, None))
            assert False
        except RepoError as re:
            assert(str(re) == "Student inexistent!")

        studenti = self.__repo_student.get_all()
        assert(len(studenti) == 1)
        assert(studenti[0] == self.__student_modificat)

    def __ruleaza_teste_repo_disciplina(self):
        self.__repo_discipline = RepoDiscipline()
        assert(len(self.__repo_discipline) == 0)
        self.__disciplina = Disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)
        self.__repo_discipline.adauga_disciplina(self.__disciplina)
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.adauga_disciplina(self.__disciplina)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina existenta")

        assert(self.__repo_discipline.cauta_disciplina_dupa_id(self.__id_disciplina) == self.__disciplina)
        self.__id_inexistent = 35236
        try:
            self.__repo_discipline.cauta_disciplina_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta")

        self.__id_disciplina_noua = 125
        self.__nume_disciplina_noua = "Haha"
        self.__profesor_nou = "Ion"
        self.__disciplina_noua = Disciplina(self.__id_disciplina_noua, self.__nume_disciplina_noua, self.__profesor_nou)
        self.__repo_discipline.adauga_disciplina(self.__disciplina_noua)
        assert(len(self.__repo_discipline) == 2)
        self.__repo_discipline.sterge_disciplina_dupa_id(self.__disciplina_noua.get_id_disciplina())
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.sterge_disciplina_dupa_id(self.__id_inexistent)
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta")

        self.__disciplina_modificata = Disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor_nou)
        self.__repo_discipline.modifica_disciplina(self.__id_disciplina, self.__disciplina_modificata)
        assert(len(self.__repo_discipline) == 1)
        try:
            self.__repo_discipline.modifica_disciplina(self.__id_inexistent, Disciplina(self.__id_inexistent, None, None))
            assert False
        except RepoError as re:
            assert(str(re) == "Disciplina inexistenta")

        discipline = self.__repo_discipline.get_all()
        assert(len(discipline) == 1)
        assert(discipline[0] == self.__disciplina_modificata)

    def __ruleaza_teste_service_studenti(self):
        self.__repo_studenti = RepoStudenti()
        self.__service_studenti = ServiceStudenti(self.__validator_student, self.__repo_studenti)
        assert (len(self.__repo_studenti) == 0)
        self.__service_studenti.adauga_student(self.__id_student, self.__nume_student)
        assert (len(self.__repo_studenti) == 1)

        studenti = self.__service_studenti.get_all_studenti()
        assert (len(studenti) == 1)
        assert (studenti[0] == self.__student)
        self.__student_modificat = Student(self.__id_student, self.__nume_student_nou)
        self.__service_studenti.modifica_student(self.__id_student, self.__nume_student_nou)
        assert(studenti[0] == self.__student_modificat)

        assert (len(self.__repo_studenti) == 1)
        self.__service_studenti.sterge_student(self.__id_student)
        assert (len(self.__repo_studenti) == 0)

        self.__service_studenti.adauga_student(self.__id_student, self.__nume_student)
        self.__service_studenti.adauga_student(self.__id_student_nou, self.__nume_student_nou)
        v = [str(x) for x in self.__service_studenti.ordoneaza_dupa_nume()]
        assert (v == ['125 Costel', '5 Vasile'])

    def __ruleaza_teste_service_disciplline(self):
        self.__repo_discipline = RepoDiscipline()
        self.__service_discipline = ServiceDiscipline(self.__validator_disciplina, self.__repo_discipline)
        assert (len(self.__repo_discipline) == 0)
        self.__service_discipline.adauga_disciplina(self.__id_disciplina, self.__nume_disciplina, self.__profesor)
        assert (len(self.__repo_discipline) == 1)
        discipline = self.__service_discipline.get_all_discipline()
        assert (len(discipline) == 1)
        assert (discipline[0] == self.__disciplina)
        self.__disciplina_modificata = Disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor)
        self.__service_discipline.modifica_disciplina(self.__id_disciplina, self.__nume_disciplina_noua, self.__profesor_nou)
        assert(discipline[0] == self.__disciplina_modificata)

        assert (len(self.__repo_discipline) == 1)
        self.__service_discipline.sterge_disciplina(self.__id_disciplina)
        assert (len(self.__repo_discipline) == 0)

    def __ruleaza_teste_repo_note(self):
        self.__repo_note = RepoNote()
        assert (len(self.__repo_note) == 0)
        self.__nota = Nota(self.__id_nota, self.__student, self.__disciplina, self.__valoare_nota)
        self.__repo_note.adauga_nota(self.__nota)
        assert (len(self.__repo_note) == 1)
        try:
            self.__repo_note.adauga_nota(self.__nota)
            assert False
        except RepoError as re:
            assert(str(re) == "Nota existenta!")

        self.__repo_note.sterge_nota_dupa_id(self.__id_nota)
        assert (len(self.__repo_note) == 0)
        try:
            self.__repo_note.sterge_nota_dupa_id(self.__id_nota)
            assert False
        except RepoError as re:
            assert(str(re) == "Nota inexistenta!")

        self.__repo_note.adauga_nota(self.__nota)

        note = self.__repo_note.get_all()
        assert (len(note) == 1)
        assert (note[0] == self.__nota)

    def __ruleaza_teste_service_note(self):
        self.__repo_discipline = RepoDiscipline()
        self.__repo_studenti = RepoStudenti()
        self.__repo_note = RepoNote()
        self.__validator_nota = ValidatorNota()
        self.__service_note = ServiceNote(self.__validator_nota, self.__repo_note, self.__repo_studenti, self.__repo_discipline)
        assert (len(self.__repo_note) == 0)
        self.__repo_studenti.adauga_student(self.__student)
        self.__repo_discipline.adauga_disciplina(self.__disciplina)
        self.__service_note.adauga_nota(self.__id_nota, self.__id_student, self.__id_disciplina, self.__valoare_nota)
        assert (len(self.__repo_note) == 1)
        self.__service_note.sterge_student_si_notele_lui(self.__id_student)
        assert (len(self.__repo_note) == 0)
        self.__id_nota_noua = 2
        self.__valoare_nota_noua = 6
        self.__repo_studenti.adauga_student(self.__student_nou)
        self.__repo_studenti.adauga_student(self.__student)
        self.__repo_discipline.adauga_disciplina(self.__disciplina_noua)
        self.__service_note.adauga_nota(self.__id_nota_noua, self.__id_student_nou, self.__id_disciplina_noua, self.__valoare_nota_noua)
        self.__service_note.adauga_nota(self.__id_nota, self.__id_student, self.__id_disciplina, self.__valoare_nota)
        assert (len(self.__repo_note) == 2)
        v = [str(x) for x in self.__service_note.ordoneaza_dupa_note()]
        lista_ordonata = ['1 5 24 7', '2 125 125 6']
        assert (lista_ordonata == v)

        assert(self.__service_note.medie_student(self.__id_student) == 7.0)
        primii20 = ['studentul:5 Vasile cu media:7.0']
        assert([str(x) for x in self.__service_note.primii20()] == primii20)

    def __blackboxtesting(self):
        self.__id_nota_medie = 10
        self.__id_nota_medie2 = 11
        self.__valoare_nota_medie1 = 7
        self.__valoare_nota_medie2 = 6
        self.__id_student_pt_medie = 3
        self.__id_disciplina_pt_medie = 3
        self.__nume_disciplina_medie = "Analizaaaa"
        self.__nume_profesor_medie = "Berindeeee"
        self.__disciplina_pt_medie = Disciplina(self.__id_disciplina_pt_medie, self.__nume_disciplina_medie, self.__nume_profesor_medie)
        self.__nume_student_medie = "Voicu"
        self.__student_medie = Student(self.__id_student_pt_medie, self.__nume_student_medie)
        self.__repo_studenti.adauga_student(self.__student_medie)
        self.__repo_discipline.adauga_disciplina(self.__disciplina_pt_medie)
        self.__service_note.adauga_nota(self.__id_nota_medie, self.__id_student_pt_medie, self.__id_disciplina_pt_medie, self.__valoare_nota_medie1)
        self.__service_note.adauga_nota(self.__id_nota_medie2, self.__id_student_pt_medie, self.__id_disciplina_pt_medie, self.__valoare_nota_medie2)
        assert (self.__service_note.medie_student(self.__id_student_pt_medie) == 6.5)
"""
