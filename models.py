from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app configuration, initalize Flask App
app = Flask(__name__)

# set up our app configs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/spotifylibrary'
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'server.py'

# init a database, db, mount it on SQLAlchemy
db = SQLAlchemy(app)

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String(150))

    def __repr__(self):
        return f'Artist(id={self.id}, name="{self.name}", bio="{self.bio}")'

    def as_dict(self):
        return {
            id: self.id,
            name: self.name, 
            bio: self.bio
        }

album_genres = db.Table('album_genres',
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True),
    db.Column('album_id', db.Integer, db.ForeignKey('albums.id'), primary_key=True)
)

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='SET NULL'))
    genres = db.relationship('Genre', secondary=album_genres, lazy='subquery',
        backref=db.backref('albums', lazy=True))

    def __repr__(self):
        return f'Artist(id={self.id}, title="{self.title}")'

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'Genre(id={self.id}, genre="{self.genre}")'
