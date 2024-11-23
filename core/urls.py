from django.urls import path
from . import views
from .views import logout_view


urlpatterns = [
    path('', views.home_view, name='home'),
    path('alumni/<int:pk>/', views.alumni_detail_view, name='alumni_detail'),
    path('student/<int:pk>/', views.student_detail_view, name='student_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('alumni/signup/', views.alumni_signup, name='alumni_signup'),
    path('student/signup/', views.student_signup, name='student_signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/alumni/', views.alumni_dashboard, name='alumni_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('mentorship/request/<int:alumni_id>/', views.mentorship_request, name='mentorship_request'),
    path('mentorship/respond/<int:request_id>/', views.respond_request, name='respond_request'),
]
