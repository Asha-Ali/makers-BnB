from lib.UserRepository import *
from lib.User import *


def test_all(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository (db_connection)
    assert repository.all() == [
        User(1, 'asha@example.com', 'password1'),
        User(2, 'lydia@example.com', 'password2'),
        User(3, 'fahim@example.com', 'password3'),
        User(4, 'gemma@example.com', 'password4')
        ]


def test_find(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find(4)
    assert user == User(4, 'gemma@example.com', 'password4')


def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None,'testemail','testpassword'))
    assert repository.all() == [
        User(1, 'asha@example.com', 'password1'),
        User(2, 'lydia@example.com', 'password2'),
        User(3, 'fahim@example.com', 'password3'),
        User(4, 'gemma@example.com', 'password4'),
        User(5, 'testemail', 'testpassword')
    ]

def test_find_by_email_when_doesnt_exist_returns_user_none(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    searched_user = repository.find_by_email("obviouslywrong@example.com")
    assert searched_user == User(None, '', '')

def test_find_by_email(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email("lydia@example.com")
    assert user == User(2, 'lydia@example.com', 'password2')



