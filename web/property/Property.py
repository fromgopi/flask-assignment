from flask import request, Blueprint

from web.commons.helper.AuthHelper import decode_jwt_token
from web.commons.helper.responses import response
from web.property.PropertyHelper import PropertyHelper

property_module = Blueprint('property', __name__)

property = PropertyHelper()


@property_module.route('/add', methods=['POST'])
def add_property():
    if request.content_type == 'application/json' and request.headers.get('Authorization'):
        token = request.headers.get('Authorization').split(" ")[-1]
        if not decode_jwt_token(token):
            return response('You dont have access to this section', 403, '')
        return property.post(request.json)
    return response('Content type must be application/json', 415, data='')


@property_module.route('/search', methods=['POST'])
def search_property():
    if request.content_type == 'application/json' and request.headers.get('Authorization'):
        return property.search(request.json)
    return response('Content type must be application/json', 415, data='')
