from flask import Blueprint, request

from web import response
from web.auth.login.LoginHelper import LoginHelper

login_module = Blueprint('login', __name__)


@login_module.route('/login', methods=['POST'])
def login():
    if request.content_type == "application/json":
        login_helper = LoginHelper()
        return login_helper.post(request.json)
    return response('Content type must be application/json', 415, data='')
