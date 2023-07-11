from flask import Blueprint, url_for

from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix= '/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list')) #question._list에 해당하는 url로 리다이렉트하도록 (url_for: 라우팅 함수명으로 url역으로 찾기, redirect: 입력받은 url로 redirect)
