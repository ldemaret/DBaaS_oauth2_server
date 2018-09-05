import bcrypt
from website.app import create_app


app = create_app({
    'SECRET_KEY': 'secret',
    'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
})


@app.cli.command()
def initdb():
    from website.models import db, User
    db.drop_all()
    db.create_all()
    db.session.add(User(username='admin', password=bcrypt.hashpw('admin'.encode('utf8'), bcrypt.gensalt())))
    db.session.add(User(username='user', password=bcrypt.hashpw('user'.encode('utf8'), bcrypt.gensalt())))
    db.session.commit()
