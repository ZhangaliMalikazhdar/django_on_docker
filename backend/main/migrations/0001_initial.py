# Generated by Django 4.2.7 on 2023-11-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('first_owner', models.IntegerField(null=True)),
                ('board_of_directors', models.TextField(null=True)),
                ('chairman_of_the_board', models.TextField(null=True)),
                ('members_of_the_board', models.TextField(null=True)),
                ('director', models.IntegerField(null=True)),
                ('chief_accountant', models.CharField(null=True)),
                ('BIN', models.IntegerField(null=True)),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=100)),
                ('mail', models.TextField(default='0')),
                ('site', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=255, null=True)),
                ('branches', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sanction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Банк второго уровня', 'Банк второго уровня'), ('Брокеры-дилеры', 'Брокеры-дилеры'), ('Кастодиан', 'Кастодиан')], default='Банк второго уровня', max_length=100)),
                ('date', models.DateField()),
                ('decision_number', models.CharField(max_length=100)),
                ('type_of_recovery', models.CharField(choices=[('Санкции и иные административные взыскания', 'Санкции и иные административные взыскания'), ('Меры надзорного реагирования', 'Меры надзорного реагирования'), ('Меры воздействия', 'Меры воздействия')], default='Меры воздействия', max_length=100)),
                ('type_of_penalty', models.CharField(choices=[('Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)', 'Меры по улучшению финансового состояния и (или) минимизации рисков (письменное предписание)'), ('Наложение административного штрафа', 'Наложение административного штрафа'), ('письменное предписание', 'письменное предписание'), ('письменное предупреждение', 'письменное предупреждение'), ('Предупреждение', 'Предупреждение'), ('письмо-обязательство', 'письмо-обязательство')], default='Наложение административного штрафа', max_length=100)),
                ('imposed_penalty', models.CharField(default='0', max_length=100)),
                ('essence_of_violation', models.CharField(default='0', max_length=100)),
                ('period_of_execution', models.CharField(default='0', max_length=20)),
                ('article', models.TextField(default='0')),
                ('note', models.TextField(default='0')),
                ('type_npa', models.TextField(default='0')),
                ('department_name', models.CharField(default='0', max_length=255)),
            ],
        ),
    ]
