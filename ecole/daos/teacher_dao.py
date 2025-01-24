from typing import Optional

from ecole.daos.dao import Dao
from ecole.models.teacher import Teacher


class TeacherDao(Dao[Teacher]):

    def create(self, teacher: Teacher) -> int:
        id_teacher = teacher.id
        return id_teacher

    def read(self, id_teacher: int) -> Optional[Teacher]:
        teacher: Optional[Teacher]
        with Dao.connection.cursor() as cursor:
            sql = ("SELECT * FROM teacher "
                   "JOIN person ON teacher.id_person = person.id_person "
                   "WHERE teacher.id_person = %s")
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'], record['last_name'], record['age'], record['hiring_date'])
            teacher.id = record['id_person']
        else:
            teacher = None
        return teacher

    def update(self, teacher: Teacher) -> bool:
        return False

    def delete(self, teacher: Teacher) -> bool:
        return False

    def read_all(self) -> list[Teacher]:
        teachers: list[Teacher]
        with Dao.connection.cursor() as cursor:
            sql = ("SELECT person.id_person, first_name, last_name, age, hiring_date FROM teacher "
                   "JOIN person ON teacher.id_person = person.id_person")
            cursor.execute(sql)
            records = cursor.fetchall()
        if records:
            teachers = [Teacher(first_name=row['first_name'], last_name=row['last_name'], age=row['age'],
                                hiring_date=row['hiring_date']) for row in records]
            for teacher, row in zip(teachers, records):
                teacher.id = row['id_person']
        else:
            teachers = []
        return teachers
