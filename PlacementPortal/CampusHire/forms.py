from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Stud_Details, User

# class StudentForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'first_name', 'last_name')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Stud_Details
        fields = ('username','college', 'cgpa','skills', 'project', 'internship', 'achievements', 'about_me')
