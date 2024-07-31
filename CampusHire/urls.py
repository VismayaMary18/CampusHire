from django.urls import path
from CampusHire import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.SignUp, name='register'),
    path('login/', views.Login, name='login'),
    path('studentview/', views.studentview, name='studentview'),
    path('placement/', views.placement, name='placement'),
    path('resources/', views.resources, name='resources'),
    path('addstudetails/', views.addstudentdetails, name='addstudetails'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('applications/', views.view_applications, name='view_applications'),
    path('job-listings/', views.job_listings, name='job_listings'),
    path('aptitude/', views.aptitude, name='aptitude'),
    path('mocktest/', views.mocktest, name='mocktest'),
    path('logout/', views.Logout, name='logout'),

]


