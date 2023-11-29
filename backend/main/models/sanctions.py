from django.db import models as m


class Sanction(m.Model):
    name = m.CharField(max_length=2550)

    TYPE = [
        ('Банк второго уровня','Банк второго уровня'),
        ('Брокеры-дилеры', 'Брокеры-дилеры'),
        ('Кастодиан', 'Кастодиан'),
    ]

    type = m.CharField(max_length=1000, choices=TYPE, default='Банк второго уровня')
    date = m.CharField(max_length=1000)
    decision_number = m.CharField(max_length=1000)

    TYPE_OF_RECOVERY = [
        ('Санкции и иные административные взыскания', 'Санкции и иные административные взыскания'),
        ('Меры надзорного реагирования', 'Меры надзорного реагирования'),
        ('Меры воздействия', 'Меры воздействия'),

    ]

    type_of_recovery = m.CharField(max_length=1000, choices=TYPE_OF_RECOVERY, default='Меры воздействия')

    IMPOSED_PENALTY = [
        ('Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)',
         'Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)'),
        ('Наложение административного штрафа', 'Наложение административного штрафа'),
        ('письменное предписание', 'письменное предписание'),
        ('письменное предупреждение', 'письменное предупреждение'),
        ('Предупреждение', 'Предупреждение'),
        ('письмо-обязательство', 'письмо-обязательство'),
    ]

    type_of_penalty = m.CharField(max_length=1000, choices=IMPOSED_PENALTY, default='Наложение административного штрафа')
    imposed_penalty = m.CharField(max_length=1000, default='0')
    essence_of_violation = m.CharField(max_length=1000, default='0')
    period_of_execution = m.CharField(max_length=1000, default='0')
    article = m.TextField(default='0')
    note = m.TextField(default='0')
    type_npa = m.TextField(default='0')
    department_name = m.CharField(max_length=2550, default='0')

    def __str__(self):
        return self.name
