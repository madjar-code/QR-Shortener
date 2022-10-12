from django.test import TestCase
from shortener.models import Link


class LinkTest(TestCase):
    def setUp(self):
        Link.objects.create(
          long_url="https://arduinomaster.ru/program/arduino-serial-print-println-write/")
        Link.objects.create(
          long_url="https://arduinomaster.ru/program/arduino-write/")
        Link.objects.create(
          long_url="https://arduinomaster.ru")
    
    def test_link_creation(self):
        link1 = Link.objects.get(long_url="https://arduinomaster.ru")
        link2 = Link.objects.get(long_url="https://arduinomaster.ru/program/arduino-write/")
        link3 = Link.objects.get(long_url="https://arduinomaster.ru/program/arduino-serial-print-println-write/")

        self.assertTrue(isinstance(link1, Link))
        self.assertTrue(isinstance(link2, Link))
        self.assertTrue(isinstance(link3, Link))

        self.assertTrue(isinstance(link1.status, str))

        self.assertTrue(link1.times_followed == 0)

    def test_times_followed_increment(self):
        link = Link.objects.get(long_url="https://arduinomaster.ru")
        link.times_followed_increment()
        self.assertTrue(link.times_followed == 1)