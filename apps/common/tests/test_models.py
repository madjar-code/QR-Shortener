from django.db import connection
from django.db.models.base import ModelBase
from django.db.utils import OperationalError
from django.test import TestCase
from common.models import TimeStampedModel


class AbstractModelMixinTestCase(TestCase):
    """
    Базовый класс для тестирования моделей
    mixin/abstract
    """
    @classmethod
    def setUpTestData(cls):
        if not hasattr(cls, 'model'):
            cls.model = ModelBase(
                '__TestModel__' +
                cls.mixin.__name__, (cls.mixin,),
                {'__module__': cls.mixin.__module__}
            )

        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(cls.model)
            super(AbstractModelMixinTestCase, cls).setUpClass()
        except OperationalError:
            pass

    @classmethod
    def tearDownClass(self):
        try:
            with connection.schema_editor() as schema_editor:
                schema_editor.delete_model(self.model)
            super(AbstractModelMixinTestCase, self).tearDownClass()
        except OperationalError:
            pass


class TimeStampedModelTest(AbstractModelMixinTestCase):
    mixin = TimeStampedModel

    def setUp(self):
        self.model.objects.create(pk=1)
    
    def test_something(self):
        model = self.model.objects.get(pk=1)
