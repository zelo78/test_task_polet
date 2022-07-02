# Generated by Django 4.0.5 on 2022-07-02 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['vehicle_registration_date'], 'verbose_name': 'транспортное средство', 'verbose_name_plural': 'транспортные средства'},
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_registration_date',
            field=models.DateField(help_text='Дата СТС (свидетельства о регистрации)', verbose_name='дата СТС'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_registration_number',
            field=models.CharField(help_text='Номер СТС (свидетельства о регистрации)', max_length=20, verbose_name='номер СТС'),
        ),
    ]
