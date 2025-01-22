# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field

from ecole.daos.course_dao import CourseDao
from ecole.daos.student_dao import StudentDao
from ecole.daos.teacher_dao import TeacherDao
from ecole.models.course import Course
from ecole.models.student import Student
from ecole.models.teacher import Teacher


@dataclass
class School:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
        - courses : liste des cours existants
        - teachers : liste des enseignants
        - students : liste des élèves
    """

    courses: list[Course] = field(default_factory=list, init=False)
    teachers: list[Teacher] = field(default_factory=list, init=False)
    students: list[Student] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours."""
        self.courses.append(course)

    def add_teacher(self, teacher: Teacher) -> None:
        """Ajout de l'enseignant teacher à la liste des enseignants."""
        self.teachers.append(teacher)

    def add_student(self, student: Student) -> None:
        """Ajout de l'élève spécifié à la liste des élèves."""
        self.students.append(student)

    def display_courses_list(self) -> None:
        """Affichage de la liste des cours avec pour chacun d'eux :
        - leur enseignant
        - la liste des élèves le suivant"""
        for course in self.courses:
            print(f"cours de {course}")
            for student in course.students_taking_it:
                print(f"- {student}")
            print()

    def display_students(self) -> None:
        print("Liste des étudiants: ")
        for student in self.students:
            print(f"- {student}, {student.address}")

    def display_teachers(self) -> None:
        print("Liste des enseignants: ")
        for teacher in self.teachers:
            print(f"- {teacher}")

    @staticmethod
    def get_course_by_id(id_course: int):
        course_dao: CourseDao = CourseDao()
        return course_dao.read(id_course)

    @staticmethod
    def get_student_by_id(id_student: int):
        student_dao: StudentDao = StudentDao()
        return student_dao.read(id_student)

    @staticmethod
    def get_teacher_by_id(id_teacher: int):
        teacher_dao: TeacherDao = TeacherDao()
        return teacher_dao.read(id_teacher)
