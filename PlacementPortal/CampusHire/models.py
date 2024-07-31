from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

from django.contrib.auth.models import User

class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    # college = models.CharField(max_length=100)
    # cgpa=models.IntegerField(default='')
    # skills = models.CharField(max_length=20)
    # project = models.CharField(max_length=100)
    # internship = models.CharField(max_length=100)
    # achievements = models.CharField(max_length=100)
    # about_me = models.CharField(max_length=100)
    # email = models.EmailField()
    # date_of_birth = models.DateField()
    # phone_number = models.CharField(max_length=20)
    # address = models.CharField(max_length=200)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.username.username
    

class Stud_Details(models.Model):
    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    cgpa=models.IntegerField(default='')
    skills = models.CharField(max_length=20)
    project = models.CharField(max_length=100)
    internship = models.CharField(max_length=100)
    achievements = models.CharField(max_length=100)
    about_me = models.CharField(max_length=100)

    def __str__(self):
        return self.username.username
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    industry = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    contact_person = models.CharField(max_length=100, default='')
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='')
    website = models.URLField(default='')
    logo = models.ImageField(upload_to='company_logos/', default='')
    company_size = models.CharField(max_length=50, default='')
    social_media_links = models.TextField(default='')

    def __str__(self):
        return self.name


class JobOpening(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    job_location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    requirements = models.TextField()
    website = models.URLField(default='')
    linkedin = models.URLField(default='')
    posted_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Extra fields
    # experience_required = models.CharField(max_length=100)
    # qualification_required = models.CharField(max_length=100)
    # skills_required = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job_opening = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, default='Submitted')

    def __str__(self):
        return f"{self.applicant.username} - {self.job_opening.title}"
    

class student_tb(models.Model):
	username=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	password1=models.CharField(max_length=100,default='')
	password2=models.CharField(max_length=100,default='')
        


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    # fname=models.CharField(max_length=30,default='')
    # lname=models.CharField(max_length=30,default='')
    # roll = models.IntegerField( blank=True)
    # address=models.TextField()
    # branch=models.TextField()
    # sem=models.IntegerField(null=True, blank=True, default=None)
    # mobile=models.IntegerField(null=True, blank=True, default=None)
    # cgpa=models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.fname
    