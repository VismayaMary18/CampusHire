from django.shortcuts import render, redirect, HttpResponse
from CampusHire.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CustomUserCreationForm
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def SignUp(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if len(uname) >12:
            messages.error(request,'User name must be under 12 characters')
            return redirect('register')
        if not uname.isalnum():
            messages.error(request,'User name must contain letters and numbers')
            return redirect('register')
        if pass1 != pass2 :
            messages.error(request,'your password is not matched correctly')
            return redirect('register')
        
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            print(uname, email, pass1, pass2)
            return redirect('login')
    return render(request, 'registration.html') 

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('passw')
        # student_details =   student_tb.from_db(username = username)
        # if user==username and :
          
        user = authenticate(request, username = username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('studentview')
        else:
            return HttpResponse("Username or Password is incorrect!!!")    
    return render(request, 'login.html')

@login_required
def view_applications(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'placement.html', {'applications': applications})


def job_listings(request):
    job_openings = JobOpening.objects.all()
    return render(request, 'jobtile.html', {'job_openings': job_openings})

def com_listings(request):
    com_details = Company.objects.all()
    return render(request, 'jobtile.html', {'com_details': com_details})

def aptitude(request):
      return render(request, 'aptitudeselection.html')

def resources(request):
      return render(request, 'resources.html')

def mocktest(request):
      return render(request, 'mocktest.html')

# @login_required(login_url = 'login')
def studentview(request):
      return render(request, 'studentview.html', {'username': request.user.username})

def placement(request):
      job_titles = JobOpening.objects.all()
      return render(request, 'placement.html', {'job_titles': job_titles})

def addstudentdetails(request):
    if request.method=='POST':
        username = request.POST.get('username')
        college = request.POST.get('college')
        cgpa = request.POST.get('cgpa')
        skills = request.POST.get('skills')
        project = request.POST.get('project')
        internship = request.POST.get('internship')
        achievements = request.POST.get('achievements')
        about_me = request.POST.get('about_me')

        query=Stud_Details(username = username, college = college, cgpa = cgpa, skills = skills, project = project, internship = internship, achievements = achievements, about_me = about_me)
        query.save()
        return redirect('addstudetails')
    else:
        return render(request, 'addstuddetails.html')

def editprofile(request):
      return render(request, 'editprofile.html')


def Logout(request):
    logout(request)
    return redirect('login')


# def register_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('homepage.html')  

#     else:
#         form = StudentForm()

#     return render(request, 'registration.html', {'form': form})


def SighUp(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        query=student_tb(username= username,email=email, password1=password1, password2 = password2)
        query.save()
        return redirect('login')
    else:
        return render(request, 'registration.html')
    




def handlesignup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        # fname=request.POST['fname']
        # lname=request.POST['lname']
        if len(username) >12:
            messages.error(request,'User name must be under 12 characters')
            return redirect('studentview')
        if not username.isalnum()  :
            messages.error(request,'User name must contain letters and numbers')
            return redirect('studentview')
        if pass1 != pass2 :
            messages.error(request,'your password is not matched correctly')
            return redirect('studentview')

        myuser = User.objects.create_user(username,email,pass1)
        # myuser.fname=fname
        # myuser.lname=lname
        myuser.save()
        
        # roll=request.POST['roll']
        # address=request.POST['address']
        # branch=request.POST['branch']
        # sem=request.POST['sem']
        # mobile=request.POST['mobile']
        # cgpa=request.POST['cgpa']
        info=Profile(username=myuser)
        info.save()
        messages.success(request,'your account has been successfully created')
        return redirect('studentview')

    else:
        return HttpResponse('Not allowed')
