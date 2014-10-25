from django.test import TestCase
from testapp.models import MyModel


class TestMirror(TestCase):
    fixtures = ['anyfixture.json']

    def test_fixture(self):
        MyModel.objects.create(name=1)
        self.assertEqual(MyModel.objects.using('default').count(),
                         MyModel.objects.using('slave').count())
