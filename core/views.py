from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Alumni, Student, MentorshipRequest
from .forms import AlumniFormStep1, AlumniFormStep2, StudentFormStep1, StudentFormStep2, MentorshipRequestForm ,AlumniProfileForm ,StudentProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower().strip()  # Normalize the email
        password = request.POST.get('password')

        # Attempt to find the user in Alumni or Student models
        user = Alumni.objects.filter(email=email).first() or Student.objects.filter(email=email).first()

        if user and user.password == password:  # Compare plain text passwords
            # Save user ID and type in session
            request.session['user_id'] = user.id
            request.session['is_alumni'] = isinstance(user, Alumni)
            request.session['is_student'] = isinstance(user, Student)
            return redirect('dashboard')  # Redirect to the dashboard view
        else:
            messages.error(request, "Invalid email or password!")

    return render(request, 'core/login.html')


@login_required
def dashboard(request):
    if request.session.get('is_alumni'):
        return redirect('alumni_dashboard')
    elif request.session.get('is_student'):
        return redirect('student_dashboard')
    return redirect('home')

    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Log the user out
        messages.success(request, "You have successfully logged out.")
    else:
        messages.info(request, "You were not logged in.")
    return redirect('login')  # Redirect to login page


@login_required
def alumni_dashboard(request):
    if not request.session.get('is_alumni'):
        return redirect('login')
    alumni = get_object_or_404(Alumni, pk=request.session.get('user_id'))
    received_requests = alumni.received_requests.all()

    # Handle Profile Update
    if request.method == 'POST' and 'edit-profile' in request.POST:
        profile_form = AlumniProfileForm(request.POST, request.FILES, instance=alumni)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('alumni_dashboard')
    else:
        profile_form = AlumniProfileForm(instance=alumni)

    context = {
        'alumni': alumni,
        'received_requests': received_requests,
        'profile_form': profile_form,
    }
    return render(request, 'core/alumni_dashboard.html', context)

@login_required
def student_dashboard(request):
    if not request.session.get('is_student'):
        return redirect('login')
    student = get_object_or_404(Student, pk=request.session.get('user_id'))
    mentorship_requests = student.mentorship_requests.all()

    # Handle Profile Update
    if request.method == 'POST' and 'edit-profile' in request.POST:
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
    else:
        profile_form = StudentProfileForm(instance=student)

    # Handle New Mentorship Request
    if request.method == 'POST' and 'new-mentorship-request' in request.POST:
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.student = student
            mentorship_request.save()
            messages.success(request, "Mentorship request submitted!")
            return redirect('student_dashboard')
    else:
        form = MentorshipRequestForm()

    context = {
        'student': student,
        'mentorship_requests': mentorship_requests,
        'profile_form': profile_form,
        'mentorship_request_form': form,
    }
    return render(request, 'core/student_dashboard.html', context)

def alumni_signup(request):
    if request.method == "POST":
        if 'step' in request.POST and request.POST['step'] == '1':
            # Process Step 1 for Alumni
            form_step1 = AlumniFormStep1(request.POST)
            form_step2 = AlumniFormStep2()
            if form_step1.is_valid():
                request.session['alumni_data'] = form_step1.cleaned_data  # Save Step 1 data in session
                return render(request, 'core/signup_alumni.html', {'form_step1': form_step1, 'form_step2': form_step2, 'step': 2})
        else:
            # Process Step 2 for Alumni
            alumni_data = request.session.get('alumni_data', {})
            form_step2 = AlumniFormStep2(request.POST, request.FILES)
            if form_step2.is_valid():
                # Combine Step 1 data with Step 2 data
                alumni = Alumni(**alumni_data, **form_step2.cleaned_data)
                alumni.save()
                messages.success(request, "Alumni account created successfully! Please log in.")
                return redirect('login')
    else:
        form_step1 = AlumniFormStep1()
        form_step2 = AlumniFormStep2()
    return render(request, 'core/signup_alumni.html', {'form_step1': form_step1, 'form_step2': form_step2, 'step': 1})

def student_signup(request):
    if request.method == "POST":
        if 'step' in request.POST and request.POST['step'] == '1':
            # Process Step 1 for Student
            form_step1 = StudentFormStep1(request.POST)
            form_step2 = StudentFormStep2()
            if form_step1.is_valid():
                request.session['student_data'] = form_step1.cleaned_data  # Save Step 1 data in session
                return render(request, 'core/signup_student.html', {'form_step1': form_step1, 'form_step2': form_step2, 'step': 2})
        else:
            # Process Step 2 for Student
            student_data = request.session.get('student_data', {})
            form_step2 = StudentFormStep2(request.POST, request.FILES)
            if form_step2.is_valid():
                # Combine Step 1 data with Step 2 data
                student = Student(**student_data, **form_step2.cleaned_data)
                student.save()
                messages.success(request, "Student account created successfully! Please log in.")
                return redirect('login')
    else:
        form_step1 = StudentFormStep1()
        form_step2 = StudentFormStep2()
    return render(request, 'core/signup_student.html', {'form_step1': form_step1, 'form_step2': form_step2, 'step': 1})


def alumni_list(request):
    alumni = Alumni.objects.all()
    return render(request, 'core/alumni_list.html', {'alumni': alumni})

def home_view(request):
    # Render the home page for unauthenticated users
    alumni_list = Alumni.objects.filter(willing_to_mentor=True)[:3]
    student_list = Student.objects.filter(interested_in_internships=True)[:3]
    return render(request, 'core/home.html', {
        'alumni_list': alumni_list,
        'student_list': student_list
    })

def alumni_detail_view(request, pk):
    alumni = get_object_or_404(Alumni, pk=pk)
    return render(request, 'core/alumni_detail.html', {'alumni': alumni})

def student_detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'core/student_detail.html', {'student': student})

def mentorship_request(request, alumni_id):
    alumni = get_object_or_404(Alumni, pk=alumni_id)
    if request.method == 'POST':
        form = MentorshipRequestForm(request.POST)
        if form.is_valid():
            mentorship_request = form.save(commit=False)
            mentorship_request.student = request.user.student
            mentorship_request.alumni = alumni
            mentorship_request.save()
            return redirect('dashboard_student')
    else:
        form = MentorshipRequestForm()
    return render(request, 'core/mentorship_request.html', {'form': form, 'alumni': alumni})

def respond_request(request, request_id):
    mentorship_request = get_object_or_404(MentorshipRequest, pk=request_id)
    if request.method == 'POST':
        if request.POST.get('action') == 'accept':
            mentorship_request.status = 'Accepted'
        elif request.POST.get('action') == 'reject':
            mentorship_request.status = 'Rejected'
        mentorship_request.save()
    return redirect('dashboard_alumni')

