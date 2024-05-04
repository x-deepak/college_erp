from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Session_Year,CustomUser, Student,Subject,Staff,Attendance,Attendance_Report
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()


    context = {
        'student_count': student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_gender_male' : student_gender_male,
        'student_gender_female' : student_gender_female,


    }
    return render(request, 'Hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

            


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic = profile_pic,
                user_type= 3,
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id= session_year,
                course_id= course, 
                gender=gender,
            )
            student.save()
            messages.success(request, 'Student Succesfully Saved')
            return redirect('add_student')


    context = { 
        'course': course,
        'session_year' : session_year,
    }

    return render(request,'Hod/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    
    context = {
        'student' : student,
    }

    return render(request, 'Hod/view_student.html',context)




@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Hod/edit_student.html',context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record is Successfully Updated !')
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_student')


@login_required(login_url='/')
def VIEW_STAFF(request):
     staff = Staff.objects.all()
    
     context = {
        'staff' : staff,
     }
     return render(request, 'Hod/view_staff.html',context)

@login_required(login_url='/')
def VIEW_ATTENDANCE(request):

    subject = Subject.objects.all()
    session_year = Session_Year.objects.all()

    action = request.GET.get('action')
    get_subject= None
    get_session_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id= session_year_id)
            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_date = attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id = attendance_id)
    context = {
        'subject' : subject,
        'session_year' : session_year,
        'action' : action,
        'get_subject' : get_subject,
        'get_session_year': get_session_year,
        'attendance_date' : attendance_date,
        'attendance_report' : attendance_report,

    }


    return render(request, 'Hod/view_attendance.html',context)