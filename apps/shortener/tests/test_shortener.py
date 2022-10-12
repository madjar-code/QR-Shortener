from django.test import TestCase
from shortener.models import Link
from shortener.shortener import Shortener


class ShortenerTest(TestCase):

    def setUp(self):
        Link.objects.create(long_url="https://arduinomaster.ru")

    def test_link_shorten(self):
        link = Link.objects.get(long_url="https://arduinomaster.ru")
        Shortener().shorten_one_link(link)
        self.assertTrue(len(link.short_url)==7)
        self.assertTrue(link.get_short_url()[:14] == 'https://liy.ru')
        self.assertTrue(link.status == 'shorter')
