from flask import request, jsonify, Blueprint
from .. import db
from .. import restless
from .. import rdb
from sample.models import User, Client, Student
from sample.validator import validate
from sample.utils import need_auth, auth_source, verify_access_token
from sample import exception
from . import utils


api_bp = Blueprint('api', __name__)


@api_bp.route('/test', methods=['GET'])
@need_auth
@auth_source
def test():
    return jsonify({
        "code": 200,
        "data": "OK"
        })


@api_bp.route('/student', methods=['GET', 'POST'])
@need_auth
@auth_source
def student():
    if request.method == 'POST':
        validate('student_create', request.json)

        student_ = Student(name=request.json['name'])
        student_.address = request.json['address']
        student_.profession = request.json['profession']

        db.session.add(student_)
        db.session.commit()

        return jsonify({
            "code": 201,
            "data": student_.to_dict()
            })

    else:
        students_ = utils.students()

        return jsonify({
            "code": 200,
            "data": students_
            })


@api_bp.route('/student/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@need_auth
@auth_source
def student_detail(id):
    if request.method == 'DELETE':
        if utils.delete_student(id):

            return jsonify({
                "code": 200,
                "data": True
                })

    elif request.method == 'PUT':
        student_ = utils.edit_student(id, request.json)

        return jsonify({
            "code": 200,
            "data": student_.to_dict()
            })

    else:
        student_ = utils.student_detail(id)

        return jsonify({
            "code": 200,
            "data": student_.to_dict()
            })