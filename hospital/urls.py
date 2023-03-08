from django.urls import path
from hospital.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hospital'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about',AboutView.as_view(),name='about'),
    path('department',DepartmentView.as_view(),name='department'),
    path('doctor-detail/<int:pk>',DoctorDetailView.as_view(),name='doctor-detail'),
    path('doctor-detail/<int:pk>',DoctorDetailView.as_view(),name='doctor-detail'),
    path('doctors',DoctorsView.as_view(),name='doctors'),
    path('appointment/<int:pk>',ShowAppointmentView.as_view(),name='appointment'),
    path('booked/<int:id>',Booked.as_view(),name='booked'),
    path('news',NewsView.as_view(),name='news'),
    path('patient-profile',PatientProfileView.as_view(),name='patient-profile'),
    path('news-detail',NewsDetailView.as_view(),name='news-detail'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)