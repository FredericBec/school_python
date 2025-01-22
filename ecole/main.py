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
    paul: Student = school.get_student_by_id(1)
    valerie: Student = school.get_student_by_id(2)
    louis: Student = school.get_student_by_id(3)

    # ajout de ceux-ci à l'école
    for student in [paul, valerie, louis]:
        school.add_student(student)

    # création des cours
    francais: Course = school.get_course_by_id(1)
    histoire: Course = school.get_course_by_id(2)
    geographie: Course = school.get_course_by_id(3)
    mathematiques: Course = school.get_course_by_id(4)
    physique: Course = school.get_course_by_id(5)
    chimie: Course = school.get_course_by_id(6)
    anglais: Course = school.get_course_by_id(7)
    sport: Course = school.get_course_by_id(8)

    # ajout de ceux-ci à l'école
    for course in [francais, histoire, geographie, mathematiques,
                   physique, chimie, anglais, sport]:
        school.add_course(course)

    # création des enseignants
    victor = school.get_teacher_by_id(4)
    jules = school.get_teacher_by_id(5)
    sophie = school.get_teacher_by_id(6)
    marie = school.get_teacher_by_id(7)
    william = school.get_teacher_by_id(8)
    michel = school.get_teacher_by_id(9)

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
    school.display_students()
    school.display_teachers()


if __name__ == '__main__':
    main()
