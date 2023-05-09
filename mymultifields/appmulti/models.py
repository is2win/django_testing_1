from django.db import models


class Forward(models.Model):
    forward_class = models.CharField(max_length=100)


class Option(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    forward = models.ForeignKey(Forward, on_delete=models.CASCADE, related_name='options')
    type_of_field = models.CharField(max_length=10,
                                     choices=(('general', 'Тип данных не известен'),
                                              ('int', 'Число целое'),
                                              ('float', 'Число с плавающей точкой'),
                                              ('dict', 'Словарь')),
                                     default='general')
