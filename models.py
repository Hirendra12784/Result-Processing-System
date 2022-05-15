# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MarksObtained(models.Model):
    roll_no = models.IntegerField()
    batch = models.ForeignKey('Subject', models.DO_NOTHING, db_column='batch')
    sem = models.IntegerField()
    course_no = models.CharField(max_length=100)
    credit_theory = models.IntegerField(blank=True, null=True)
    credit_practical = models.IntegerField(blank=True, null=True)
    midterm_marks = models.IntegerField()
    theory_marks = models.IntegerField()
    practical_marks = models.IntegerField()
    grade_point = models.IntegerField(blank=True, null=True)
    credit_points = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'marks_obtained'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=70, blank=True, null=True)
    father_name = models.CharField(max_length=70, blank=True, null=True)
    mother_name = models.CharField(max_length=70, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    eno = models.CharField(unique=True, max_length=70, blank=True, null=True)
    bdate = models.DateField(blank=True, null=True)
    sem = models.IntegerField(blank=True, null=True)
    rno = models.IntegerField(unique=True, max_length=70, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dno = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'student'


class Subject(models.Model):
    batch = models.CharField(primary_key=True, max_length=20)
    sem_no = models.IntegerField()
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=200, blank=True, null=True)
    credit = models.IntegerField()
    mid_marks = models.IntegerField()
    th_marks = models.IntegerField()
    pract_marks = models.IntegerField()

    class Meta:
        #managed = False
        db_table = 'subject'
        unique_together = (('course_code'),)
