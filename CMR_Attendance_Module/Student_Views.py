from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Student,Subject,Attendance,Attendance_Report,Course



@login_required(login_url='/')
def HOME(request):
    #pie data
    student = Student.objects.get(admin = request.user.id)
    
    programme = Course.objects.get(name=student.course_id)

    
    total_classes = 0
    for i in Subject.objects.filter(course=programme):
        # print(i)
        total_classes +=  Attendance.objects.filter(subject_id=i.id).count()
        # print(total_classes)

    total_present = Attendance_Report.objects.filter(student_id = student).count()
    total_absent = total_classes - total_present
    # print(total_present)

    #box data
    
    program = student.course_id
    course_count = Subject.objects.filter(course=programme).count()

    context = {
        
        'program':program,
        'course_count' : course_count,
        'total_present':total_present,
        'total_absent':total_absent,

    }


    return render(request,'Student/home.html',context)


@login_required(login_url='/')
def STUDENT_VIEW_ATTENDANCE(request):

    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)

    action = request.GET.get('action')
    get_subject = None
    attendance_report = None
    
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id=subject_id)

            attendance_report = Attendance_Report.objects.filter(student_id=student,attendance_id__subject_id = subject_id)

    context = {
            'subjects' : subjects,
            'action' : action,
            'get_subject' : get_subject,
            'attendance_report' : attendance_report,
    }

    return render(request, 'Student/view_attendance.html',context)