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
