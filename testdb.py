from pybo.models import Question, Answer
from datetime import datetime
from pybo import db

def test():
    q = Question(subject='질문1입니다.', content='질문1에 대한 내용', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()

def test1():
    for x in range(1, 11):
        q = Question(subject='질문 %d제목' %x, content='질문 %d입니다.' %x, create_date=datetime.now())
        db.session.add(q)
    db.session.commit()

def getall_question():
    # result = Question.query.all()
    # for tmp in result:
    #     print(tmp.subject)
    #     print(tmp.content)
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()