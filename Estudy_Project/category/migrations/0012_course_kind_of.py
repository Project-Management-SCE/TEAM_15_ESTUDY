# Generated by Django 3.2.5 on 2022-04-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_auto_20220421_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='kind_of',
            field=models.CharField(choices=[('1', 'הרצאות'), ('2', ',תרגולים'), ('3', 'עבודות בית'), ('3', 'מבחנים'), ('5', 'YouTube'), ('6', 'Zoom')], default='1', max_length=30),
        ),
    ]