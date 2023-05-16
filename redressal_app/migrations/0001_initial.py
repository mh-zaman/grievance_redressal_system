# Generated by Django 4.2.1 on 2023-05-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('admin_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=25)),
                ('admin_email', models.EmailField(max_length=50, unique=True)),
                ('admin_image', models.ImageField(blank=True, null=True, upload_to='admins/')),
                ('admin_contact', models.CharField(max_length=11)),
                ('admin_address', models.CharField(max_length=255)),
                ('admin_designation', models.CharField(max_length=255)),
                ('admin_department', models.CharField(max_length=255)),
                ('admin_password', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'admin_users',
            },
        ),
        migrations.CreateModel(
            name='ComplaintModel',
            fields=[
                ('compalint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_subject', models.CharField(max_length=255)),
                ('compalint_description', models.TextField()),
                ('compalint_status', models.CharField(max_length=255)),
                ('complaint_progress', models.CharField(max_length=255)),
                ('complaint_total', models.IntegerField()),
                ('compalint_resolved', models.IntegerField()),
                ('complaint_pending', models.IntegerField()),
                ('complaint_raised', models.IntegerField()),
                ('complainer_id', models.CharField(max_length=13)),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50)),
                ('faculty_email', models.EmailField(max_length=50, unique=True)),
                ('faculty_image', models.ImageField(blank=True, null=True, upload_to='faculties/')),
                ('faculty_contact', models.CharField(max_length=11)),
                ('faculty_address', models.CharField(max_length=255)),
                ('faculty_designation', models.CharField(max_length=255)),
                ('faculty_department', models.CharField(max_length=255)),
                ('faculty_password', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'faculty_users',
            },
        ),
        migrations.CreateModel(
            name='ProctorModel',
            fields=[
                ('proctor_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('proctor_name', models.CharField(max_length=50)),
                ('proctor_email', models.EmailField(max_length=50, unique=True)),
                ('proctor_image', models.ImageField(blank=True, null=True, upload_to='proctors/')),
                ('proctor_contact', models.CharField(max_length=11)),
                ('proctor_address', models.CharField(max_length=255)),
                ('proctor_designation', models.CharField(max_length=255)),
                ('proctor_department', models.CharField(max_length=255)),
                ('proctor_password', models.CharField(max_length=25)),
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
                ('student_image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('student_contact', models.CharField(max_length=11)),
                ('student_address', models.CharField(max_length=255)),
                ('student_department', models.CharField(max_length=255)),
                ('student_password', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'student_users',
            },
        ),
    ]