# Generated by Django 4.2.2 on 2023-08-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampusHire', '0004_remove_student_email_remove_student_major_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopening',
            name='linkedin',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='jobopening',
            name='website',
            field=models.URLField(default=''),
        ),
    ]
