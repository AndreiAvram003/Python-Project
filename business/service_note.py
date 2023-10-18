from domeniu.note import Nota
from domeniu.primii20 import Primii20


class ServiceNote:

    def __init__(self, validator_nota, repo_note, repo_studenti, repo_discipline):
        self.__validator_nota = validator_nota
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    def adauga_nota(self, id_nota, id_student, id_disciplina, valoare):
        """

        :param id_nota: id-ul notei care va fi adaugate
        :param id_student: studentul care va primi nota cu id_nota
        :param id_disciplina: disciplnia la care va primi nota
        :param valoare: valoarea notei
        :return: nota a fost adaugata
        """
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        disciplina = self.__repo_discipline.cauta_disciplina_dupa_id(id_disciplina)
        nota = Nota(id_nota, student, disciplina, valoare)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)

    def get_all(self):
        """

        :return: totalitatea notelor
        """
        return self.__repo_note.get_all()

    def sterge_student_si_notele_lui(self, id_student):
        """

        :param id_student: id-ul studentului care va fi sters , alaturi de notele lui
        :return: studentul si notele acestuia au fost sterse
        """
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_student() == student]
        for nota_student in note_student:
            self.__repo_note.sterge_nota_dupa_id(nota_student.get_id_nota())
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def ordoneaza_dupa_note(self):
        """

        :return: Notele ordonate descrescator
        """
        note = self.__repo_note.get_all()
        note_ordonate = sorted(note, key=lambda nota: nota.get_nota(), reverse=True)
        return note_ordonate


    def medie_student(self, id_student):
        """

        :param id_student: id-ul studentului caruia ii calculez media
        :return: media studentului
        """
        note = self.__repo_note.get_all()
        s = 0
        c = 0
        for nota in note:
            if nota.get_student().get_id_student() == id_student:
                s = s + nota.get_nota()
                c = c + 1
        media = s/c
        return media

    def primii20(self):
        """

        :return: primii 20% din studenti , dupa mediile acestora
        """
        primii_20 = []
        informatii_studenti = []
        note = self.__repo_note.get_all()
        for nota in note:
            student = nota.get_student()
            id_student = student.get_id_student()
            if student not in informatii_studenti:
                medie_student = self.medie_student(id_student)
                medie = Primii20(student, medie_student)
                if medie not in primii_20:
                    primii_20.append(medie)
                informatii_studenti.append(student)
        primii_20.sort(reverse=True)
        k = int(len(informatii_studenti)/5)
        if k == 0:
            k = 1
        return primii_20[:k]

    def studenti_la_disc(self, k):
        informatii_studenti = []
        c = 0
        note = self.__repo_note.get_all()
        for nota in note:
            student = nota.get_student()
            disciplina = nota.get_disciplina()
            if student not in informatii_studenti:
                if disciplina.get_nume()[0] == k:
                    c = c+1
                    informatii_studenti.append(student)
        return c
