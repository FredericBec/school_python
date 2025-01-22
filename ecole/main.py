#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from datetime import date

from models.address import Address
from models.course import Course
from models.teacher import Teacher
from models.student import Student
from business.school import School


def init_school(school: School) -> None:
    """Initialisation d'un jeu de test pour l'école school."""
    # création des étudiants et rattachement à leur adresse
    paul: Student    = Student('Paul', 'Dubois', 12)
    valerie: Student = Student('Valérie', 'Dumont', 13)
    louis: Student   = Student('Louis', 'Berthot', 11)

    paul.adress    = Address('12 rue des Pinsons', 'Castanet', 31320)
    valerie.adress = Address('43 avenue Jean Zay', 'Toulouse', 31200)
    louis.adress   = Address('7 impasse des Coteaux', 'Cornebarrieu', 31150)

    # ajout de ceux-ci à l'école
    for student in [paul, valerie, louis]:
        school.add_student(student)

    # création des cours
    francais: Course = Course("Français", date(2024, 1, 29),
                                          date(2024, 2, 16))
    histoire: Course = Course("Histoire", date(2024, 2, 5),
                                          date(2024, 2, 16))
    geographie: Course = Course("Géographie", date(2024, 2, 5),
                                              date(2024, 2, 16))
    mathematiques: Course = Course("Mathématiques", date(2024, 2, 12),
                                                    date(2024, 3, 8))
    physique: Course = Course("Physique", date(2024, 2, 19),
                                          date(2024, 3, 8))
    chimie: Course = Course("Chimie", date(2024, 2, 26),
                                      date(2024, 3, 15))
    anglais: Course = Course("Anglais", date(2024, 2, 12),
                                        date(2024, 2, 24))
    sport: Course = Course("Sport", date(2024, 3, 4),
                                    date(2024, 3, 15))

    # ajout de ceux-ci à l'école
    for course in [francais, histoire, geographie, mathematiques,
                   physique, chimie, anglais, sport]:
        school.add_course(course)

    # création des enseignants
    victor  = Teacher('Victor', 'Hugo', 23, date(2023, 9, 4))
    jules   = Teacher('Jules', 'Michelet', 32, date(2023, 9, 4))
    sophie  = Teacher('Sophie', 'Germain', 25, date(2023, 9, 4))
    marie   = Teacher('Marie', 'Curie', 31, date(2023, 9, 4))
    william = Teacher('William', 'Shakespeare', 34, date(2023, 9, 4))
    michel  = Teacher('Michel', 'Platini', 42, date(2023, 9, 4))

    # ajout de ceux-ci à l'école
    for teacher in [victor, jules, sophie, marie, william, michel]:
        school.add_teacher(teacher)

    # association des élèves aux cours qu'ils suivent
    for course in [geographie, physique, anglais]:
        paul.add_course(course)

    for course in [francais, histoire, chimie]:
        valerie.add_course(course)

    for course in [mathematiques, physique, geographie, sport]:
        louis.add_course(course)

    # association des enseignants aux cours qu'ils enseignent
    victor.add_course(francais)

    jules.add_course(histoire)
    jules.add_course(geographie)

    sophie.add_course(mathematiques)

    marie.add_course(physique)
    marie.add_course(chimie)

    william.add_course(anglais)

    michel.add_course(sport)


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    init_school(school)

    # affichage de la liste des cours, leur enseignant et leurs élèves
    school.display_courses_list()

    print(school.get_course_by_id(1))
    print(school.get_course_by_id(2))
    print(school.get_course_by_id(9))


if __name__ == '__main__':
    main()
