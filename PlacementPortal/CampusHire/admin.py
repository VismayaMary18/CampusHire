from django.contrib import admin
from .models import *

# Register your models here.

class StudentDetails(admin.ModelAdmin):
    list_display = ('username', 'college',  'cgpa','skills', 'project', 'internship', 'achievements', 'about_me')

class CompanyDetails(admin.ModelAdmin):
    list_display = ('name','description','industry','location','contact_person','email','phone','website','logo','company_size','social_media_links')


class JobOpeningsAdmin(admin.ModelAdmin):
    list_display = ('title','company','description','job_location','salary','requirements','posted_date','is_active')

class SignUpAdmin(admin.ModelAdmin):
    list = ('username', 'email', 'password1','password2')


admin.site.register(Company, CompanyDetails)
admin.site.register(JobOpening, JobOpeningsAdmin)
admin.site.register(Stud_Details, StudentDetails)
admin.site.register(student_tb, SignUpAdmin)
