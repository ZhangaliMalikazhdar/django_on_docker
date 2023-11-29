from django.db import models as m


class Sanction(m.Model):
    name = m.CharField(max_length=255)

    TYPE = [
        ('Банк второго уровня','Банк второго уровня'),
        ('Брокеры-дилеры', 'Брокеры-дилеры'),
        ('Кастодиан', 'Кастодиан'),
    ]

    type = m.CharField(max_length=100, choices=TYPE, default='Банк второго уровня')
    date = m.DateField()
    decision_number = m.CharField(max_length=100)

    TYPE_OF_RECOVERY = [
        ('Санкции и иные административные взыскания', 'Санкции и иные административные взыскания'),
        ('Меры надзорного реагирования', 'Меры надзорного реагирования'),
        ('Меры воздействия', 'Меры воздействия'),

    ]

    type_of_recovery = m.CharField(max_length=100, choices=TYPE_OF_RECOVERY, default='Меры воздействия')

    IMPOSED_PENALTY = [
        ('Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)',
         'Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)'),
        ('Наложение административного штрафа', 'Наложение административного штрафа'),
        ('письменное предписание', 'письменное предписание'),
        ('письменное предупреждение', 'письменное предупреждение'),
        ('Предупреждение', 'Предупреждение'),
        ('письмо-обязательство', 'письмо-обязательство'),
    ]

    type_of_penalty = m.CharField(max_length=100, choices=IMPOSED_PENALTY, default='Наложение административного штрафа')
    imposed_penalty = m.CharField(max_length=100, default='0')
    essence_of_violation = m.CharField(max_length=100, default='0')
    period_of_execution = m.CharField(max_length=20, default='0')
    article = m.TextField(default='0')
    note = m.TextField(default='0')
    type_npa = m.TextField(default='0')
    department_name = m.CharField(max_length=255, default='0')
