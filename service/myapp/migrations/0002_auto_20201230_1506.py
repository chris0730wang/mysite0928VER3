# Generated by Django 3.1.1 on 2020-12-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeforeYouReadAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=2)),
                ('number', models.IntegerField()),
                ('numofchoose1', models.IntegerField()),
                ('numofchoose2', models.IntegerField()),
                ('numofchoose3', models.IntegerField()),
                ('numofchoose4', models.IntegerField()),
                ('numofchoose5', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FocusOnContentAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('lesson', models.IntegerField()),
                ('questionnum', models.CharField(default=None, max_length=100)),
                ('correctoption', models.CharField(max_length=100)),
                ('chooseoption1', models.IntegerField()),
                ('chooseoption2', models.IntegerField()),
                ('chooseoption3', models.IntegerField()),
                ('chooseoption4', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyPreviewAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('lesson', models.IntegerField()),
                ('questionnum', models.CharField(max_length=100)),
                ('correctoption', models.CharField(max_length=100)),
                ('chooseoption1', models.IntegerField()),
                ('chooseoption2', models.IntegerField()),
                ('chooseoption3', models.IntegerField()),
                ('chooseoption4', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VocabularyReviewAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('lesson', models.IntegerField()),
                ('questionnum', models.CharField(max_length=100)),
                ('correctoption', models.CharField(max_length=100)),
                ('chooseoption1', models.IntegerField()),
                ('chooseoption2', models.IntegerField()),
                ('chooseoption3', models.IntegerField()),
                ('chooseoption4', models.IntegerField()),
                ('totalchoose', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='student',
            new_name='studentcheck',
        ),
        migrations.DeleteModel(
            name='ReadAloud',
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.RenameField(
            model_name='vocabularypreview',
            old_name='mean',
            new_name='option1',
        ),
        migrations.RemoveField(
            model_name='vocabularypreview',
            name='speech',
        ),
        migrations.RemoveField(
            model_name='vocabularypreview',
            name='wordquestion',
        ),
        migrations.AddField(
            model_name='focusoncontent',
            name='lesson',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='focusoncontent',
            name='questionnum',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='focusoncontent',
            name='unit',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularypreview',
            name='option2',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularypreview',
            name='option3',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularypreview',
            name='option4',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularypreview',
            name='question',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularypreview',
            name='questionnum',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularyreview',
            name='lesson',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularyreview',
            name='questionnum',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vocabularyreview',
            name='unit',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beforeyouread',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='beforeyouread',
            name='unit',
            field=models.CharField(max_length=2),
        ),
    ]
