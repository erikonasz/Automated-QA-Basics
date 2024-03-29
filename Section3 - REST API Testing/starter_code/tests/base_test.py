from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self) -> None:
        return super().setUp(self)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
             db.init_app(app)
             db.create_all()
        self.app = app.test_client()
        self.app_context = app.test_context = app.app_context
        
        pass

    def tearDown(self) -> None:
        with app.app_context():
            db.session.remove()
            db.drop_all()
        pass