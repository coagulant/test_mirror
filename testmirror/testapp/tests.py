from django.test import TestCase
from testapp.models import MyModel


class TestMirror(TestCase):

    def test_fixture(self):
        MyModel.objects.using('default').create(name=1)
        MyModel.objects.using('slave').create(name=2)
        MyModel.objects.using('slave').create(name=3)
        self.assertEqual(list(map(repr, MyModel.objects.using('default').all())),
                         list(map(repr, MyModel.objects.using('slave').all())))
