from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('display/', views.display, name='display'),
    path('add/', views.Add, name='add_student'),
    path('student_form/', views.Add_Student_Page, name='student_page'),
    path('read/', views.Read, name='read_student'),
    path('update/<int:rollno>/', views.update, name='update_student'),
    path('delete/<int:Roll_no>/', views.delete, name='delete_student'),
    path('dashboard/', views.dashboard, name='dashboard'),

    
]
