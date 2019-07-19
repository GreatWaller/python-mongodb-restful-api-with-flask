import mongoengine as me

class Imdb(me.EmbeddedDocumentField):
    imdb_id = me.StringField()
    rating = me.DecimalField()
    votes = me.IntField()

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()
    imdb = me.EmbeddedDocumentField(Imdb)
