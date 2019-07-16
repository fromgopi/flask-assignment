from flask import make_response, jsonify
import json


def response(message, status_code, data):
    """
    Helper method to make an Http response
    :param data:
    :param message: Message
    :param status_code: Http status code
    :return:
    """
    return make_response(jsonify({
        'message': message,
        'data': data
    })), status_code


def response_auth(status, message, token, status_code):
    """
    Make a Http response to send the auth token
    :param status: Status
    :param message: Message
    :param token: Authorization Token
    :param status_code: Http status code
    :return: Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message,
        'auth_token': token.decode("utf-8")
    })), status_code
