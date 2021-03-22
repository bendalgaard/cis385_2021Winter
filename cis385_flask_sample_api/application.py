from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_cors import CORS

# Create the Flask application and the Flask-SQLAlchemy object.
# this needs to be called application for ElasticBeanStalk, not app
application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/data.db'
cors = CORS(application, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(application)
ma = Marshmallow(application)
api = Api(application)

# Flask-SQLALchemy models
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    birth_date = db.Column(db.Date)

    def __repr__(self):
        return '<Person %s>' % self.name

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content= db.Column(db.Unicode)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    owner = db.relationship('Person', backref=db.backref('notes', lazy='dynamic'))

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    vendor = db.Column(db.Unicode)
    purchase_time = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    owner = db.relationship('Person', backref=db.backref('computers', lazy='dynamic'))

class PersonSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "birth_date")
        model = Person

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

class PersonListResource(Resource):
    def get(self):
        persons = Person.query.all()
        return persons_schema.dump(persons)

    def post(self):
        new_person = Person(
            name=request.json['name'],
            birth_date=datetime.strptime(request.json['birth_date'], '%Y-%m-%d')
        )
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person)


class PersonResource(Resource):
    def get(self, person_id):
        person = Person.query.get_or_404(person_id)
        return person_schema.dump(person)

    def patch(self, person_id):
        person = Person.query.get_or_404(person_id)

        if 'name' in request.json:
            person.name = request.json['name']
        if 'birth_date' in request.json:
            person.birth_date = datetime.strptime(request.json['birth_date'], '%Y-%m-%d')

        db.session.commit()
        return person_schema.dump(person)

    def delete(self, person_id):
        person = Person.query.get_or_404(person_id)
        db.session.delete(person)
        db.session.commit()
        return '', 204


api.add_resource(PersonListResource, '/person')
api.add_resource(PersonResource, '/person/<int:person_id>')




class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.Unicode)
    content= db.Column(db.Unicode)
    priority = db.Column(db.SmallInteger)
    due_date = db.Column(db.Date)

    def __repr__(self):
        return '<Note %s>' % self.title

class NoteSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content", "priority", "due_date")
        model = Note

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)

class NoteListResource(Resource):
    def get(self):
        notes = Note.query.all()
        return notes_schema.dump(notes)

    def post(self):
        new_note = Note(
            title=request.json['title'],
            content=request.json['content'],
            priority=request.json['priority'],
            due_date=datetime.strptime(request.json['due_date'], '%Y-%m-%d')
        )
        db.session.add(new_note)
        db.session.commit()
        return note_schema.dump(new_note)


class NoteResource(Resource):
    def get(self, note_id):
        note = Note.query.get_or_404(note_id)
        return note_schema.dump(note)

    def patch(self, note_id):
        note = Note.query.get_or_404(note_id)

        if 'title' in request.json:
            note.title = request.json['title']

        db.session.commit()
        return note_schema.dump(note)

    def delete(self, note_id):
        note = Note.query.get_or_404(note_id)
        db.session.delete(note)
        db.session.commit()
        return '', 204


api.add_resource(NoteListResource, '/note')
api.add_resource(NoteResource, '/note/<int:note_id>')






class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName= db.Column(db.Unicode)
    lastName= db.Column(db.Unicode)
    title= db.Column(db.Unicode)
    quantity = db.Column(db.SmallInteger)
    year = db.Column(db.SmallInteger)

    def __repr__(self):
        return '<Book %s>' % self.title

class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstName", "lastName", "title", "quantity", "year")
        model = Book

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books)

    def post(self):
        new_book = Book(
            firstName=request.json['firstName'],
            lastName=request.json['lastName'],
            title=request.json['title'],
            quantity=request.json['quantity'],
            year=request.json['year']
        )
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book)


class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book_schema.dump(book)

    def patch(self, book_id):
        book = Book.query.get_or_404(book_id)

        if 'title' in request.json:
            book.title = request.json['title']

        db.session.commit()
        return book_schema.dump(book)

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204


api.add_resource(BookListResource, '/book')
api.add_resource(BookResource, '/book/<int:book_id>')



# Create the database tables.
db.create_all()


# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: '<h2 id="welcome"></h2><script>document.getElementById("welcome").innerHTML = "<p>This is a REST application.</p><p>Try the following command from a (bash) terminal: </p><p> curl -XGET " + window.location.href + "api/person</p>"</script>'))

# start the flask loop
# run the app.
if __name__ == "__main__":
    # application.DEBUG = True
    application.run()
