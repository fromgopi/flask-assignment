from flask import request, Blueprint

from web.auth.register.RegisterHelper import RegisterHelper
from web.commons.helper.responses import response

register_module = Blueprint('register', __name__)


@register_module.route('/signup', methods=['POST'])
def signup():
    if request.content_type == 'application/json':
        register = RegisterHelper()
        return register.post(request.json)
    return response('Content type must be application/json', 415, data='')
