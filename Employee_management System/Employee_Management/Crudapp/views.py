from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required




def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard/')
            else:
                return render(request, 'login.html', {'message': 'Invalid credentials'})
        return render(request, 'login.html')
    except Exception as e:
       
        return render(request, 'login.html', {'message': 'An error occurred during login'})


def signup(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'message': 'Username already exists'})
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('login')
        return render(request, 'signup.html')
    except Exception as e:
        return render(request, 'signup.html', {'message': 'An error occurred during signup'})


def logout(request):
    try:
        auth.logout(request)
        return render(request, 'login.html')
    except Exception as e:
        logger.exception("Error during logout")
        return render(request, 'login.html', {'message': 'An error occurred during logout'})



@login_required(login_url='login')
def display(request):
    try:
        students = Student.objects.all()
        return render(request, 'Student.html', {"std": students})
    except Exception as e:
        return render(request, 'Student.html', {'message': 'Unable to display student list'})


@login_required(login_url='login')
def Add(request):
    try:
        if request.method == "POST":
            roll_no = request.POST.get('Rollno')
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            department = request.POST.get('Department')

            if Student.objects.filter(Roll_no=roll_no).exists():
                return render(request, 'add.html', {'message': 'Roll number already exists'})
            elif Student.objects.filter(Email=email).exists():
                return render(request, 'add.html', {'message': 'Email already exists'})
            else:
                Student.objects.create(Roll_no=roll_no, Name=name, Email=email, Department=department)
                return redirect('/display/')
        return render(request, 'add.html')
    except Exception as e:
        
        return render(request, 'add.html', {'message': 'An error occurred while adding student'})


@login_required(login_url='login')
def Add_Student_Page(request):
    return render(request, 'add.html')


@login_required(login_url='login')
def Read(request):
    try:
        if request.method == "POST":
            roll_no = request.POST.get('Rollno')
            student = Student.objects.get(Roll_no=roll_no)
            all_students = Student.objects.all()
            return render(request, 'Student.html', {"Student": student, "std": all_students})
        return render(request, 'Student.html')
    except Student.DoesNotExist:
        return render(request, 'Student.html', {'message': 'Student not found'})
    except Exception as e:
       
        return render(request, 'Student.html', {'message': 'An error occurred while reading student data'})


@login_required(login_url='login')
def update(request, rollno):
    try:
        std = get_object_or_404(Student, Roll_no=rollno)

        if request.method == "POST":
            std.Name = request.POST.get("Name")
            std.Email = request.POST.get("Email")
            std.Department = request.POST.get("Department")
            std.save()
            return redirect('/display/')

        return render(request, 'update_information.html', {'std': std})
    except Exception as e:
        
        return render(request, 'update_information.html', {'message': 'An error occurred while updating'})


@login_required(login_url='login')
def delete(request, Roll_no):
    try:
        if request.method == "POST":
            student = Student.objects.get(Roll_no=Roll_no)
            student.delete()
            return redirect('/display/')
        return render(request, 'Student.html')
    except Student.DoesNotExist:
        return render(request, 'Student.html', {'message': 'Student not found'})
    except Exception as e:
        
        return render(request, 'Student.html', {'message': 'An error occurred while deleting student'})




def homepage(request):
    try:
        return render(request, 'Student.html')
    except Exception as e:
        
        return render(request, 'Student.html', {'message': 'An error occurred while loading page'})



def dashboard(request):
    if request.method=='POST':
        return render(request,'dashboard.html')
    return render(request,'dashboard.html')