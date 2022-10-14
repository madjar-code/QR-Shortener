import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from files.api.serializers import SessionSerializer
from files.models import Session


client = Client()


class GetAllSessionsTest(TestCase):

    def setUp(self):
        Session.objects.create()
        Session.objects.create()
        Session.objects.create()

    def test_get_all_sessions(self):
        response = client.get(reverse('all-sessions'))
        sessions = Session.objects.all()
        serializer = SessionSerializer(
          sessions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateExcelTest(TestCase):

    def setUp(self):
        self.invalid_payload = {
            'input_file':
            '../REPORT.xlsx'
        }
        self.valid_payload = {
            'input_file':
            './all_images/REPORT.xlsx'
        }
    
    def test_start_invalid_shortening(self):
        response = client.post(
            reverse('start-shortening'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        invalid_message = {'error': 'Incorrect data'}
        self.assertEqual(response.data, invalid_message)

    def test_start_valid_shortening(self):
        response = client.post(
            reverse('start-shortening'),
            data = json.dumps(self.valid_payload),
            content_type='application/json'
        )
        pass