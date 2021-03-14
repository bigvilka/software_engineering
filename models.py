from app import db


class Note(db.Document):
    meta = {'collection': 'notes'}
    id = db.SequenceField(primary_key=True)
    title = db.StringField()
    content = db.StringField()

    def create_note(self, title, content):
        result = {}
        if title:
            self.title = title
            result.update({'title': title})
        if content:
            self.content = content
            result.update({'content': content})
        self.save()
        result.update({'id': self.id})
        return result