# Generated by Django 3.2.5 on 2022-04-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220421_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', 'זכר'), ('2', 'נקבה')], max_length=10, null=True),
        ),
    ]
