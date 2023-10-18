from domeniu.student import Student
from infrastructura.file_repo_studenti import FileRepoStudenti


class Teste:

    def ruleaza_toate_testele(self):
        self.__ruleaza_toate_testele()

    def __goleste_fisier(self, calea_catre_fisier):
        with open(calea_catre_fisier, "w") as f:
            pass

    def __ruleaza_toate_testele(self):
        calea_catre_teste_file = "teste/teste_studenti.txt"
        self.__goleste_fisier(calea_catre_teste_file)
        repo = FileRepoStudenti(calea_catre_teste_file)
        assert repo.get_size() == 0
        student = Student(1, "David")
        repo.adauga_student(student)
        assert repo.get_size() == 1
