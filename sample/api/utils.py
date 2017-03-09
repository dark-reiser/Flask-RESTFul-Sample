from flask import request, abort
from .. import rdb
from .. import db
from sample.models import Student
from sample import exception


def students():
    return [student.to_dict() for student in Student.query.all()]


def delete_student(id):
    student = Student.query.filter(Student.id == id).first()

    if not student:
        abort(403)

    db.session.delete(student)
    db.session.commit()

    return True


def edit_student(id, data):
    support_keys = ['name', 'address', 'profession']

    student = Student.query.filter(Student.id == id).first()
    for key in support_keys:
        d = data.get(key, None)
        if d is not None:
            setattr(student, key, d)

    db.session.add(student)
    db.session.commit()

    return student

def student_detail(id):
    student = Student.query.filter(Student.id == id).first()

    if not student:
        abort(404)

    return student