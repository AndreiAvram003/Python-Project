import unittest

from business.service_note import ServiceNote
from infrastructura.file_repo_studenti import FileRepoStudenti
from infrastructura.repo_note import RepoNote
from validare.validator_nota import ValidatorNota
from validare.validator_student import ValidatorStudent
from validare.validator_disciplina import ValidatorDisciplina
from infrastructura.repo_studenti import RepoStudenti
from infrastructura.repo_discipline import RepoDiscipline
from business.service_studenti import ServiceStudenti
from business.service_discipline import ServiceDiscipline
from prezentare.consola import UI
from teste.teste import Teste


def main():
    validator_student = ValidatorStudent()
    validator_disciplina = ValidatorDisciplina()
    validator_nota = ValidatorNota()
    """calea_catre_studenti = "studenti.txt"
    repo_studenti = FileRepoStudenti(calea_catre_studenti)
    for student in repo_studenti.get_all():
        print(student)"""
    repo_studenti = RepoStudenti()
    repo_discipline = RepoDiscipline()
    repo_note: RepoNote = RepoNote()
    service_studenti = ServiceStudenti(validator_student, repo_studenti)
    service_discipline = ServiceDiscipline(validator_disciplina, repo_discipline)
    service_note = ServiceNote(validator_nota, repo_note, repo_studenti, repo_discipline)
    consola = UI(service_studenti, service_discipline, service_note)
    teste = Teste()

    teste.ruleaza_toate_testele()
    consola.run()
    unittest.main()


main()
