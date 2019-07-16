from web import response
from web.auth.models.AuthModel import AuthModel
from web.commons.helper import AuthHelper
from web.commons.helper.AuthHelper import validate_password


class LoginHelper:
    def post(self, json_payload):
        resp = {}
        email = json_payload['email']
        password = json_payload['password']
        auth_model = AuthModel()

        # Check if the user registered or not.
        user = auth_model.check_for_user(email)
        if user:
            if not validate_password(user.password, password):
                return response("Invalid Password", 400, data='')
            jwt_token = self.generate_auth_token(user.id)
            resp = {
                "email": user.email,
                "jwt": "Bearer " + str(jwt_token)
            }
            return response('Login Successfully', 200, data=resp)
        return response("We could'nt find the email", 401, data='http://localhost:5000/singup')

    def generate_auth_token(self, auth_id):
        return AuthHelper.generate_jwt_token(auth_id)
