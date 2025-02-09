# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field

from daos.course_dao import CourseDao
from daos.student_dao import StudentDao
from daos.teacher_dao import TeacherDao
from models.course import Course
from models.student import Student
from models.teacher import Teacher


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
        for course in self.get_all_courses():
            print(f"cours de {course}")
            for student in course.students_taking_it:
                print(f"- {student}")
            print()

    def display_students(self) -> None:
        """Display students list"""
        print("Liste des étudiants: ")
        for student in self.get_all_students():
            print(f"- {student}")

    def display_teachers(self) -> None:
        """Display teachers list"""
        print("Liste des enseignants: ")
        for teacher in self.get_all_teachers():
            print(f"[{teacher.id}] - {teacher}")

    @staticmethod
    def get_course_by_id(id_course: int):
        """
        Retrieve a course in database
        :param id_course: id
        :return: course
        """
        course_dao: CourseDao = CourseDao()
        return course_dao.read(id_course)

    @staticmethod
    def get_student_by_id(id_student: int):
        """
        Retrieve a student
        :param id_student: id of student
        :return: result of request
        """
        student_dao: StudentDao = StudentDao()
        return student_dao.read(id_student)

    @staticmethod
    def get_teacher_by_id(id_teacher: int):
        """
        Retrieve a teacher
        :param id_teacher: id
        :return: result of request
        """
        teacher_dao: TeacherDao = TeacherDao()
        return teacher_dao.read(id_teacher)

    @staticmethod
    def get_all_students() -> list[Student]:
        """
        Retrieve all students
        :return: student list
        """
        student_dao: StudentDao = StudentDao()
        return student_dao.read_all()

    @staticmethod
    def get_all_teachers() -> list[Teacher]:
        """
        Retrieve all teachers
        :return: teacher list
        """
        teacher_dao: TeacherDao = TeacherDao()
        return teacher_dao.read_all()

    @staticmethod
    def get_all_courses() -> list[Course]:
        """
        Retrieve all courses
        :return: course list
        """
        course_dao: CourseDao = CourseDao()
        return course_dao.read_all()
