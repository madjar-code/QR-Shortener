import uuid
from django.test import TestCase
from django.db.models.fields import FilePathField
from files.models import Session


class SessionTest(TestCase):
    def setUp(self):
        Session.objects.create(input_file='text.txt')

    def test_session_creation(self):
        session = Session.objects.all().first()
        self.assertTrue(isinstance(session, Session))
        self.assertTrue(
            session.input_file,
            FilePathField)

    def test_path_derivation(self):
        session = Session.objects.all().first()
        self.assertTrue(
          session.get_output_file_url() ==\
             '127.0.0.1:8000/media/')
        self.assertTrue(
          session.get_zip_file_url() ==\
             '127.0.0.1:8000/media/')
