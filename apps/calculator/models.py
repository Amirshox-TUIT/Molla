from django.db import models

class CalculatorModel(models.Model):
    first_num = models.IntegerField()
    second_num = models.IntegerField()
    amal = models.CharField(max_length=2)
    result = models.FloatField()

    def __str__(self):
        return f'{self.first_num} {self.amal} {self.second_num} = {self.result}'

    class Meta:
        verbose_name = 'Calculator'
        verbose_name_plural = 'Calculators'


