from domeniu.disciplina import Disciplina
from infrastructura.repo_discipline import RepoDiscipline


class FileRepoDiscipline(RepoDiscipline):

    def __init__(self, locatie_fisier):
        RepoDiscipline.__init__(self)
        self.__locatie_fisier = locatie_fisier

    def __read_all_from_file(self):
        with open(self.__locatie_fisier, "r") as f:
            lines = f.readlines()
            self.__discipline.clear()
            for line in lines:
                if line != "":
                    line = line.strip()
                    parti = line.split(" ")
                    id_disciplina = int(parti[0])
                    nume = parti[1]
                    profesor = parti[2]
                    disciplina = Disciplina(id_disciplina, nume, profesor)
                    self.__discipline[id] = disciplina

    def __write_all_to_file(self):
        with open(self.__locatie_fisier, "w") as f:
            for disciplina in self.__discipline.values():
                f.write(str(disciplina) + "\n")

    def adauga_disciplina(self, disciplina):
        self.__read_all_from_file()
        RepoDiscipline.adauga_disciplina(self, disciplina)
        self.__write_all_to_file()

    def sterge_disciplina_dupa_id(self, id_disciplina):
        self.__read_all_from_file()
        RepoDiscipline.sterge_disciplina_dupa_id(self, id_disciplina)
        self.__write_all_to_file()

    def cauta_disciplina_dupa_id(self, id_disciplina):
        self.__read_all_from_file()
        return RepoDiscipline.cauta_disciplina_dupa_id(self, id_disciplina)

    def modifica_disciplina(self, id_disciplina, disciplina_noua):
        self.__read_all_from_file()
        RepoDiscipline.modifica_disciplina(self, id_disciplina, disciplina_noua)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoDiscipline.get_all(self)

    def __len__(self):
        return len(self.__discipline)

    def get_size(self):
        return len(self.get_all())
