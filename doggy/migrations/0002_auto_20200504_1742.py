# Generated by Django 3.0.4 on 2020-05-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='adaptability',
            field=models.IntegerField(null=True, verbose_name='적응력'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='confidence',
            field=models.IntegerField(null=True, verbose_name='자신감'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='independence',
            field=models.IntegerField(null=True, verbose_name='자립심'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='positive',
            field=models.IntegerField(null=True, verbose_name='긍정 마인드'),
        ),
        migrations.AddField(
            model_name='dogs',
            name='shynewss',
            field=models.IntegerField(null=True, verbose_name='부끄러움'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='description',
            field=models.TextField(null=True, verbose_name='테스트 결과 설명'),
        ),
    ]
