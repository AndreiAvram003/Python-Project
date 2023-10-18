import string
import random
from domeniu.disciplina import Disciplina


class ServiceDiscipline:

    def __init__(self, validator_disciplina, repo_discipline):
        self.__validator_disciplina = validator_disciplina
        self.__repo_discipline = repo_discipline

    def adauga_disciplina(self, id_disciplina, nume, profesor):
        """

        :param id_disciplina: id-ul disciplinei care va fi adaugat
        :param nume:  numele disciplinei
        :param profesor: numele profesorului
        :return:  studentul a fost adaugat
        """
        disciplina = Disciplina(id_disciplina, nume, profesor)
        self.__validator_disciplina.valideaza(disciplina)
        self.__repo_discipline.adauga_disciplina(disciplina)

    def get_all_discipline(self):
        """

        :return: preluarea tuturor disciplinelor
        """
        return self.__repo_discipline.get_all()

    def sterge_disciplina(self, id_disciplina):
        """

        :param id_disciplina: id-ul studentului care va fi sters
        :return: studentul a fost sters
        """
        self.__repo_discipline.sterge_disciplina_dupa_id(id_disciplina)

    def modifica_disciplina(self, id_disciplina, nume_nou, profesor_nou):
        """

        :param id_disciplina: id-ul disciplinei care va fi modificat
        :param nume_nou: numele modificat
        :param profesor_nou:  profesorul modificat
        :return: Disciplina a fost modificata
        """
        disciplina_noua = Disciplina(id_disciplina, nume_nou, profesor_nou)
        self.__repo_discipline.modifica_disciplina(id_disciplina, disciplina_noua)

    def genereaza_random(self, n):
        """

        :param n: numarul de discipline generate
        :return: Disciplinele au fost generate
        """
        while n > 0:
            try:
                id_random = random.randint(1, 1000 + self.__repo_discipline.get_size())
                nume_random = (''.join(random.choice(string.ascii_lowercase) for x in range(10)))
                profesor_random = (''.join(random.choice(string.ascii_lowercase) for x in range(10)))
                disciplina_random = Disciplina(id_random, nume_random, profesor_random)
                self.__validator_disciplina.valideaza(disciplina_random)
                self.__repo_discipline.adauga_disciplina(disciplina_random)
            except ValueError:
                continue
            n = n - 1
