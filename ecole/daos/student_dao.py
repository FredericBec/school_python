from typing import Optional

from ecole.daos.dao import Dao
from ecole.models.address import Address
from ecole.models.student import Student


class StudentDao(Dao[Student]):

    def create(self, student: Student) -> int:
        id_student = student.id
        return id_student

    def read(self, id_student: int) -> Optional[Student]:
        student: Optional[Student]
        with Dao.connection.cursor() as cursor:
            sql = ("SELECT * FROM student "
                   "JOIN person ON student.id_person = person.id_person "
                   "JOIN address ON address.id_address = person.id_address "
                   "WHERE student.id_person=%s")
            cursor.execute(sql, (id_student,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'], record['last_name'], record['age'])
            student.address = Address(record['street'], record['city'], record['postal_code'])
            student.id = record['id_person']
        else:
            student = None
        return student

    def update(self, student: Student) -> bool:
        return False

    def delete(self, student: Student) -> bool:
        return False

    def read_all(self):
        students: list[Student]
        with Dao.connection.cursor() as cursor:
            sql = ("SELECT first_name, last_name, age FROM student "
                   "JOIN person ON student.id_person = person.id_person")
            cursor.execute(sql)
            records = cursor.fetchall()
        if records:
            students = [Student(first_name=row['first_name'], last_name=row['last_name'], age=row['age'])
                        for row in records]
        else:
            students = []

        return students
