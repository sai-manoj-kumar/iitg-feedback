__author__ = 'saimanoj'

from google.appengine.ext import db


class FormA(db.Model):
    keyPhrase = db.StringProperty(required = True)
    rating2_1 = db.IntegerProperty(required = True)
    rating2_2 = db.IntegerProperty(required = True)
    rating2_3 = db.IntegerProperty(required = True)
    rating3_1 = db.IntegerProperty(required = True)
    rating3_2 = db.IntegerProperty(required = True)
    rating3_3 = db.IntegerProperty(required = True)
    rating3_4 = db.IntegerProperty(required = True)
    rating3_5 = db.IntegerProperty(required = True)
    rating3_6 = db.IntegerProperty(required = True)
    rating4_1 = db.IntegerProperty(required = True)
    rating4_2 = db.IntegerProperty(required = True)
    rating4_3 = db.IntegerProperty(required = True)
    rating4_4 = db.IntegerProperty(required = True)
    rating4_5 = db.IntegerProperty(required = True)
    rating4_6 = db.IntegerProperty(required = True)
    rating4_7 = db.IntegerProperty(required = True)
    rating4_8 = db.IntegerProperty(required = True)
    rating4_9 = db.IntegerProperty(required = True)
    rating4_10 = db.IntegerProperty(required = True)
    rating5_1 = db.IntegerProperty(required = True)
    rating5_2 = db.IntegerProperty(required = True)
    rating5_3 = db.IntegerProperty(required = True)
    rating5_4 = db.IntegerProperty(required = True)
    rating5_5 = db.IntegerProperty(required = True)
    comment = db.StringProperty()


class FormB(db.Model):
    keyPhrase = db.StringProperty(required = True)
    rating2_1 = db.IntegerProperty(required = True)
    rating2_2 = db.IntegerProperty(required = True)
    rating2_3 = db.IntegerProperty(required = True)
    rating2_4 = db.IntegerProperty(required = True)
    rating2_5 = db.IntegerProperty(required = True)
    rating3_1 = db.IntegerProperty(required = True)
    rating3_2 = db.IntegerProperty(required = True)
    rating3_3 = db.IntegerProperty(required = True)
    rating3_4 = db.IntegerProperty(required = True)
    rating3_5 = db.IntegerProperty(required = True)
    rating3_6 = db.IntegerProperty(required = True)
    rating3_7 = db.IntegerProperty(required = True)
    rating3_8 = db.IntegerProperty(required = True)
    rating3_9 = db.IntegerProperty(required = True)
    rating3_10 = db.IntegerProperty(required = True)
    comment = db.StringProperty()


class Keys(db.Model):
    keyPhrase = db.StringProperty(required = True)
    formFilled = db.BooleanProperty(required = True)
    timestamp = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def by_name(cls, key):
        return cls.all().filter('keyPhrase = ', key).get()

