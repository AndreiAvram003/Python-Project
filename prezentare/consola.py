from erori.repo_error import RepoError
from erori.validation_error import ValidError


class UI:

    def __init__(self, service_studenti, service_discipline, service_note):
        self.__service_studenti = service_studenti
        self.__service_discipline = service_discipline
        self.__service_note = service_note
        self.__comenzi = {
            "adauga_student": self.__ui_adauga_student,
            "afisare_studenti": self.__ui_afisare_studenti,
            "sterge_student": self.__ui_sterge_student,
            "sterge_student_si_notele_lui": self.__ui_sterge_student_si_notele_lui,
            "modifica_student": self.__ui_modifica_student,
            "random_student": self.__ui_random_student,
            "adauga_disciplina": self.__ui_adauga_disciplina,
            "afisare_discipline": self.__ui_afisare_disciplina,
            "sterge_disciplina": self.__ui_sterge_disciplina,
            "modifica_disciplina": self.__ui_modifica_disciplina,
            "random_disciplina": self.__ui_random_disciplina,
            "ordoneaza_studenti": self.__ui_ordoneaza_dupa_nume,
            "adauga_nota": self.__ui_adauga_nota,
            "afisare_note": self.__ui_afisare_note,
            "ordoneaza_dupa_note": self.__ui_ordoneaza_dupa_note,
            "afisare_primii20": self.__ui_primii20,
            "ordoneaza_descrescator": self.__ui_ordoneaza_descrescator

        }

    def __ui_adauga_student(self):
        if len(self.__parametri) != 2:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__parametri[0])
        nume = self.__parametri[1]
        self.__service_studenti.adauga_student(id_student, nume)
        print("Student adaugat cu succes!")

    def __ui_afisare_studenti(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        studenti = self.__service_studenti.get_all_studenti()
        if len(studenti) == 0:
            print("Nu exista studenti in aplicatie!")
            return
        for student in studenti:
            print(student)

    def __ui_sterge_student(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__parametri[0])
        self.__service_studenti.sterge_student(id_student)
        print(f"Studentul cu id-ul {id_student} a fost sters cu succes!")

    def __ui_sterge_student_si_notele_lui(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__parametri[0])
        self.__service_note.sterge_student_si_notele_lui(id_student)
        print(f"Studentul cu id-ul {id_student} si notele lui au fost sterse cu succes!")

    def __ui_modifica_student(self):
        if len(self.__parametri) != 2:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__parametri[0])
        nume_nou = self.__parametri[1]
        self.__service_studenti.modifica_student(id_student, nume_nou)
        print(f"Studentul cu id-ul {id_student} a fost modificat cu succes!")

    def __ui_random_student(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        else:
            n = int(self.__parametri[0])
            self.__service_studenti.genereaza_random(n)

    def __ui_adauga_disciplina(self):
        if len(self.__parametri) != 3:
            print("Numar parametri invalid!")
            return
        id_disciplina = int(self.__parametri[0])
        nume = self.__parametri[1]
        profesor = self.__parametri[2]
        self.__service_discipline.adauga_disciplina(id_disciplina, nume, profesor)
        print("Disciplina adaugata cu succes!")

    def __ui_afisare_disciplina(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        discipline = self.__service_discipline.get_all_discipline()
        if len(discipline) == 0:
            print("Nu exista discipline in aplicatie!")
        for disciplina in discipline:
            print(disciplina)

    def __ui_sterge_disciplina(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        id_disciplina = int(self.__parametri[0])
        self.__service_discipline.sterge_disciplina(id_disciplina)
        print(f"Disciplina cu id-ul {id_disciplina} a fost stearsa cu succes!")

    def __ui_modifica_disciplina(self):
        if len(self.__parametri) != 3:
            print("Numar parametri invalid!")
            return
        id_disciplina = int(self.__parametri[0])
        nume_nou = self.__parametri[1]
        profesor_nou = self.__parametri[2]
        self.__service_discipline.modifica_disciplina(id_disciplina, nume_nou, profesor_nou)
        print(f"Disciplina cu id-ul {id_disciplina} a fost modificata cu succes!")

    def __ui_random_disciplina(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        n = int(self.__parametri[0])
        self.__service_discipline.genereaza_random(n)

    def __ui_adauga_nota(self):
        if len(self.__parametri) != 4:
            print("Numar parametri invalid!")
            return
        id_nota = int(self.__parametri[0])
        id_student = int(self.__parametri[1])
        id_disciplina = int(self.__parametri[2])
        valoare = float(self.__parametri[3])
        self.__service_note.adauga_nota(id_nota, id_student, id_disciplina, valoare)
        print("Nota adaugata cu succes!")

    def __ui_afisare_note(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        note = self.__service_note.get_all()
        if len(note) == 0:
            print("Nu exista note in aplicatie!")
        for nota in note:
            print(nota)

    def __ui_ordoneaza_dupa_nume(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        studenti_ordonati = self.__service_studenti.ordoneaza_dupa_nume()
        for student in studenti_ordonati:
            print(student)

    def __ui_ordoneaza_descrescator(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        studenti_ordonati_descrescator = self.__service_studenti.ordoneaza_descrescator()
        for student in studenti_ordonati_descrescator:
            print(student)

    def __ui_primii20(self):
        primii20 = self.__service_note.primii20()
        for primu in primii20:
            print(primu)

    """def __ui_studenti_la_disc(self):
        if len(self.__parametri) != 1:
            print("Numar parametri invalid!")
            return
        n = str(self.__parametri[0])
        print(self.__service_note.studenti_la_disc(n))"""

    def __ui_ordoneaza_dupa_note(self):
        if len(self.__parametri) != 0:
            print("Numar parametri invalid!")
            return
        note_ordonate = self.__service_note.ordoneaza_dupa_note()
        for nota in note_ordonate:
            print(nota)

    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()  # strip elimina caracterele invizibile de la inceput sau de la final
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__parametri = parti[1:]  # sau parametri comenzii vor fi parti[1]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: Tip numeric invalid!")
                except ValidError as ve:
                    print(f"Valid Error:{ve}")  # daca punem un f in fata ghilimelelor si in acolade{} punem ve, acesta
# aplica automat str pe el
                except RepoError as re:
                    print(f"Repo Error:{re}")  # ca sa stim de unde a crapat eroarea
            else:
                print("Comanda invalida!")
