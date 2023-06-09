# Generated by Django 3.0.4 on 2020-04-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myforms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=264)),
            ],
        ),
        migrations.RenameModel(
            old_name='AccessRecords',
            new_name='AccessRecord',
        ),
    ]
