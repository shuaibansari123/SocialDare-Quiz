# Generated by Django 4.0.1 on 2022-03-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsappRatingDare', '0003_remove_personownchart_q11_remove_personownchart_q12_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answermodel',
            name='answer_for',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]