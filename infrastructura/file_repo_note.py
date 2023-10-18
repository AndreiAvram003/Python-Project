from domeniu.noteDTO import NotaDTO
from infrastructura.repo_note import RepoNote


class FileRepoNote(RepoNote):

    def __init__(self, locatie_fisier):
        RepoNote.__init__(self)
        self.__locatie_fisier = locatie_fisier

    def __read_all_from_file(self):
        with open(self.__locatie_fisier, "r") as f:
            lines = f.readlines()
            self.__note.clear()
            for line in lines:
                if line != "":
                    line = line.strip()
                    parti = line.split(" ")
                    id_nota = int(parti[0])
                    id_student = int(parti[1])
                    id_disciplina = int(parti[2])
                    valoare = float(parti[3])
                    nota = NotaDTO(id_nota, id_student, id_disciplina, valoare)
                    self.__note[id_nota] = nota

    def __write_all_to_file(self):
        with open(self.__locatie_fisier, "w") as f:
            for nota in self.__note.values():
                f.write(str(nota) + "\n")

    def adauga_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__write_all_to_file()

    def sterge_nota_dupa_id(self, id_nota):
        self.__read_all_from_file()
        RepoNote.sterge_nota_dupa_id(self, id_nota)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def __len__(self):
        return len(self.__note)
