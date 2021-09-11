# -*- coding: utf-8 -*-
from flask import make_response, jsonify


def response_success_data(data):
    return {'code': 200, 'msg': '操作成功', 'data': data}


def response_success_no_data():
    return {'code': 200, 'msg': '操作成功'}


def response_error_data(msg, code):
    return {'msg': msg, 'code': code}


def make_response_success_no_data():
    return make_response(jsonify(response_success_no_data()), 200)


def make_response_success(data):
    return make_response(jsonify(response_success_data(data)), 200)


# --------------------------  通用错误码 -----------------------------------

def make_response_400():
    return make_response(jsonify(response_error_data('请求无效', 400)), 400)


def make_response_401():
    return make_response(jsonify(response_error_data('权限不足', 401)), 401)


def make_response_403():
    return make_response(jsonify(response_error_data('禁止访问', 403)), 403)


def make_response_404():
    return make_response(jsonify(response_error_data('请求不存在', 404)), 404)


def make_response_500():
    return make_response(jsonify(response_error_data('无法连接到服务器', 500)), 500)


def make_response_1000():
    return make_response(jsonify(response_error_data('操作失败', 1000)), 200)







