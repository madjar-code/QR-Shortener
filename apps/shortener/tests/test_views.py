import json
from uuid import UUID
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from shortener.models import LinkTemplate
from shortener.models import Link
from shortener.api.serializers import LinkTemplateSerializer


client = Client()


class GetAllTemplatesTest(TestCase):

    def setUp(self):
        LinkTemplate.objects.create(
            name="Шаблон 1",
            url="https://arduinomaster.ru/program/arduino-serial-print-println-write/")
        LinkTemplate.objects.create(
            name="Шаблон 2",
            url="https://arduinomaster.ru/program/arduino-write/")
        LinkTemplate.objects.create(
            name="Шаблон 3",
            url="https://arduinomaster.ru")

    def test_get_all_templates(self):
        response = client.get(reverse('templates'))
        templates = LinkTemplate.objects.all()
        serializer = LinkTemplateSerializer(
            templates, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class getShortUrlTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'long_url': 'https://youtube.com',
        }

    def test_create_short_url(self):
        response = client.post(
            reverse('long-url'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['short url'][:14] == 'https://liy.ru')
        self.assertTrue(isinstance(response.data['session id'], UUID))
