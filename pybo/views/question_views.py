from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from ..import db
from ..models import Question
from ..forms import QuestionForm, AnswerForm
from pybo.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc()) #질문 목록 데이터를 작성일시 기준으로 역순 정렬
    question_list = question_list.paginate(page=page, per_page = 10)
    return render_template('question/question_list.html', question_list = question_list) #render_template: 템플릿 파일을 화면으로 렌더링

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods = ('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit(): 
        #request.method: create 함수로 요청된 전송 방식
        #form.validate_on_submit() 전송된 폼 데이터의 정합성을 점검하는 함수
        question = Question(subject = form.subject.data, content = form.content.data, create_date = datetime.now(), user = g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
        #POST 요청이고 폼 데이터에 이상이 없을 경우 질문을 저장한 뒤 main.index 페이지로 이동
    return render_template('question/question_form.html', form = form)

@bp.route('/modify/<int:question_id>/', methods = ('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method == 'POST': #POST 요청
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else: #GET 요청
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)
    
@bp.route('/delete/<int:question_id>/')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question._list'))

@bp.route('/vote/<int:question_id>/')
@login_required
def vote(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash('본인이 작성한 글은 추천할 수 없습니다')
    else:
        _question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))