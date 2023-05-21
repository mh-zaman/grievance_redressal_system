# Generated by Django 4.2.1 on 2023-05-19 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintModel',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_subject', models.CharField(max_length=255)),
                ('compalint_description', models.CharField(max_length=2555)),
                ('complaint_status', models.CharField(max_length=255)),
                ('complainer_id', models.CharField(max_length=50)),
                ('complainer_name', models.CharField(max_length=50)),
                ('complainer_email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'complaints',
            },
        ),
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('faculty_id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(max_length=50)),
                ('faculty_email', models.EmailField(max_length=50, unique=True)),
                ('faculty_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('faculty_contact', models.CharField(max_length=15)),
                ('faculty_address', models.CharField(max_length=255)),
                ('faculty_designation', models.CharField(max_length=255)),
                ('faculty_department', models.CharField(max_length=255)),
                ('faculty_password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'faculty_users',
            },
        ),
        migrations.CreateModel(
            name='HandlerModel',
            fields=[
                ('handler_id', models.AutoField(primary_key=True, serialize=False)),
                ('handler_name', models.CharField(max_length=25)),
                ('handler_email', models.EmailField(max_length=50, unique=True)),
                ('handler_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('handler_contact', models.CharField(max_length=15)),
                ('handler_address', models.CharField(max_length=255)),
                ('handler_password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'handler_users',
            },
        ),
        migrations.CreateModel(
            name='ProctorModel',
            fields=[
                ('proctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('proctor_name', models.CharField(max_length=50)),
                ('proctor_email', models.EmailField(max_length=50, unique=True)),
                ('proctor_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('proctor_contact', models.CharField(max_length=15)),
                ('proctor_address', models.CharField(max_length=255)),
                ('proctor_designation', models.CharField(max_length=255)),
                ('proctor_department', models.CharField(max_length=255)),
                ('proctor_password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'proctor_users',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('student_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=50, unique=True)),
                ('student_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('student_contact', models.CharField(max_length=15)),
                ('student_address', models.CharField(max_length=255)),
                ('student_department', models.CharField(max_length=255)),
                ('student_password', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'student_users',
            },
        ),
    ]
