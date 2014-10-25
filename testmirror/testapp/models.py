from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return '<MyModel: %s>' % self.name
