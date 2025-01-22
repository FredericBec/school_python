# -*- coding: utf-8 -*-

"""
Classe Teacher
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import date
from .person import Person
from .course import Course


@dataclass
class Teacher(Person):
    """Enseignant d'un ou plusieurs cours de l'école :
    - id              : clé primaire de l'entité persistante
    - hiring_date     : date d'arrivée dans l'école
    - courses_teached : cours qu'il ou elle enseigne
    """
    id: Optional[int] = field(default=None, init=False)
    hiring_date: date
    courses_teached: list[Course] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        course.teacher = self

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, arrivé(e) le {self.hiring_date}"
