from datetime import datetime
from conf import db, ma



FRUIT_LIST = ['mango', 'orange']


class Fruit(db.Model):
    __tablename__ = "fruit"
    date = db.Column(db.Integer, primary_key=True)
    mango = db.Column(db.Integer)
    orange = db.Column(db.Integer)
    content = {}
    # def __init__ (self, date, content):
    #     self.date = date
        # self.content = content
        # print(content)
        # for key, value in content.items():
        #     key = db.Column(db.Integer)
        #     key = value
    # date = db.Column(db.Integer)
    


class fruitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Fruit
        sqla_session = db.session