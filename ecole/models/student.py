# -*- coding: utf-8 -*-

"""
Classe Student, fille de la classe Person
"""

from dataclasses import dataclass, field
from typing import ClassVar
from .person import Person
from .course import Course


@dataclass
class Student(Person):
    """Elève suivant un ou plusieurs cours de l'école :
    - students_nb   : nombre total d'élèves
    - student_nbr   : n° d'élève
    - courses_taken : liste des cours pris par cet élève
    """
    students_nb: ClassVar[int] = 0  # nb d'étudiants créés
    student_nbr: int = field(init=False)
    courses_taken: list[Course] = field(default_factory=list, init=False)

    def __post_init__(self):
        """Détermination du n° de l'élève créé."""
        Student.students_nb += 1
        self.student_nbr = Student.students_nb

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours suivis par l'élève."""
        self.courses_taken.append(course)
        course.students_taking_it.append(self)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, n° étudiant : {self.student_nbr}"
