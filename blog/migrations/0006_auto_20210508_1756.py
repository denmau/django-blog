# Generated by Django 3.2 on 2021-05-08 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210508_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='date_created',
        ),
    ]