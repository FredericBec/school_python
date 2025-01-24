# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""


from dataclasses import dataclass
from typing import Optional

from ecole.daos.dao import Dao
from ecole.daos.teacher_dao import TeacherDao
from ecole.models.course import Course
from ecole.models.teacher import Teacher


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours obj

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué).
        """
        ...
        return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]
        with Dao.connection.cursor() as cursor:
            sql = "SELECT * FROM course WHERE id_course=%s"
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is not None:
            course = Course(record['name'], record['start_date'], record['end_date'])
            course.id = record['id_course']
        else:
            course = None

        return course

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True

    def read_all(self) -> list[Course]:
        """
        Retrieve all course datas in the database by sending a request
        :return: a list of course
        """
        courses = list[Course]
        with Dao.connection.cursor() as cursor:
            sql = ("SELECT name, start_date, end_date, p.first_name, p.last_name, p.age, t.hiring_date FROM course "
                   "JOIN teacher AS t ON t.id_teacher = course.id_teacher "
                   "JOIN person AS p ON p.id_person = t.id_person ")
            cursor.execute(sql)
            records = cursor.fetchall()
        if records:
            courses = [Course(name=row['name'], start_date=row['start_date'], end_date=row['end_date'])
                       for row in records]
            for course, row in zip(courses, records):
                course.teacher = Teacher(first_name=row['first_name'], last_name=row['last_name'], age=row['age'],
                                         hiring_date=row['hiring_date'])
        return courses
