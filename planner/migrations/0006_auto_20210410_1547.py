# Generated by Django 3.1.7 on 2021-04-10 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0005_auto_20210410_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='planner.course')),
                ('Semester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='planner.semester')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.AddConstraint(
            model_name='student_plan',
            constraint=models.UniqueConstraint(fields=('Semester', 'Course', 'Student'), name='Course exists'),
        ),
    ]
