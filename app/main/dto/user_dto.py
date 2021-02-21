from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'public_id': fields.String(description='user Identifier')
    })
