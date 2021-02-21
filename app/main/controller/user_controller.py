from flask import request
from flask_restplus import Resource
from app.dto.user_dto import UserDto

from app.service.user_service import (
    save_new_user,
    get_all_users,
    get_a_user
)

api = UserDto.api
user_model = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.marshal_with(user_model, envelope='data')
    def get(self):
        return get_all_users()
