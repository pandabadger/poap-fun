# Generated by Django 3.0.7 on 2020-08-04 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notificationsubscription',
            unique_together=set(),
        ),
    ]
