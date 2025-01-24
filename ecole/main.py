#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
import time
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


def valid_integer(prompt: str, min_int: int, max_int: int) -> int:
    """
    Verify if the user enter the right entry
    :param prompt: question to the user
    :param min_int: value minimum
    :param max_int: value maximum
    :return:
    """
    valid_number: bool = False
    number: int = 0

    print(prompt)
    while not valid_number:
        number_str: str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_number = (min_int <= number <= max_int)
            if not valid_number:
                print(f"Merci de saisir un nombre entier compris entre {min_int} et {max_int}")
        else:
            print("Merci de saisir un nombre entier positif !")

    return number


def research_student(school: School):
    """Method for search a student in database and displaying the result of request"""
    school.display_students()
    research = input("Veuillez saisir le numéro d'étudiant: \n")
    request = school.get_student_by_id(int(research))
    if request is not None:
        print(request)
    else:
        print("Veuillez saisir un numéro valide!")


def research_teacher(school: School):
    """Method for search a teacher in database and displaying the result of request"""
    school.display_teachers()
    research = input("Veuillez saisir l'id: \n")
    request = school.get_teacher_by_id(int(research))
    if request is not None:
        print(request)
    else:
        print("Veuillez saisir un numéro valide!")


def main_menu(school: School) -> None:
    """Display main menu and ask user to choose an action"""
    is_continue = True
    enter_key_str = "Saisir la touche Entrée pour continuer"
    while is_continue:
        print("""\
        --------------------------
        Bienvenue dans notre école
        --------------------------""")

        print("[1] - Afficher la liste des cours")
        print("[2] - Afficher la liste des étudiants")
        print("[3] - Afficher la liste des enseignants")
        print("[4] - Rechercher un étudiant")
        print("[5] - Rechercher un enseignant")
        print("[6] - Quitter l'application")

        user_choice: int = valid_integer("Que souhaitez-vous faire?", 1, 6)
        match user_choice:
            case 1:
                school.display_courses_list()
                input(enter_key_str)
            case 2:
                school.display_students()
                input(enter_key_str)
            case 3:
                school.display_teachers()
                input(enter_key_str)
            case 4:
                research_student(school)
            case 5:
                research_teacher(school)
            case 6:
                is_continue = False
                exit()


def main() -> None:
    """Programme principal."""
    school: School = School()
    # init_school(school)
    main_menu(school)


if __name__ == '__main__':
    main()
