# Generated by Django 4.1.7 on 2023-04-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_stdaddress_alter_student_stdemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stdBirth',
            field=models.DateField(),
        ),
    ]
