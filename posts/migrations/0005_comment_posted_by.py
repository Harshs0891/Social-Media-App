# Generated by Django 5.0 on 2024-02-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='harsh', max_length=100),
            preserve_default=False,
        ),
    ]
