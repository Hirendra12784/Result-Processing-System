from django.contrib import admin
from .models import MarksObtained,Student,Subject

admin.site.register(Student)
admin.site.register(MarksObtained)
admin.site.register(Subject)