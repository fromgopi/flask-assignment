from web.auth.models.AuthModel import AuthModel
from web.commons.helper.responses import response


class RegisterHelper:
    def post(self, json_payload):
        resp = {}
        auth_model = AuthModel()
        print(json_payload['password'])
        user_check = auth_model.check_for_user(json_payload['email'])
        if user_check:
            return response('Failed, User already exists, Please sign In', 400, user_check.email)
        user_data = auth_model.create_user(json_payload)
        if user_data['code'] != 200:
            return response('Unable to process now!.', user_data['code'], '')
        return response('Successfully registered', user_data['code'], data=user_data['email'])