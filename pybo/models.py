from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)
class Question(db.Model): #질문 모델
    id = db.Column(db.Integer, primary_key=True) #고유 번호
    subject = db.Column(db.String(200), nullable=False) #제목
    content = db.Column(db.Text(), nullable=False) #내용
    create_date = db.Column(db.DateTime(), nullable=False) #작성 일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set')) #글쓴이 정보 추가하기
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

class Answer(db.Model): #답변 모델
    id = db.Column(db.Integer, primary_key=True) #고유 번호
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) #답변을 질문과 연결하는 foreign key (데이터베이스에서는 기존 모델과 연결된 속성을 외부 키라고 한다)
    question = db.relationship('Question', backref=db.backref('answer_set')) #질문 모델을 참조하기 위해 추가: db.relationship('참조할 모델명', 역참조 설정)
    content = db.Column(db.Text(), nullable=False) #내용
    create_date = db.Column(db.DateTime(), nullable=False) #작성 일시
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set')) #글쓴이 정보 추가하기
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
