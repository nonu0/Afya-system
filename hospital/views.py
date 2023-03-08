from django.shortcuts import render
from hospital.models import Doctor,Patient,Appointment,AppointmentItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,DetailView
from django.core.exceptions import ValidationError
from django.contrib import messages
# Create your views here.


class DoctorsView(LoginRequiredMixin,TemplateView):
    next_page  = 'hospital:doctors.html'
    template_name = 'doctors.html'
    login_url = 'authentication:login'
    redirect_field_name = 'doctors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.all()
        context['doctors'] = doctors
        return context
class DoctorDetailView(LoginRequiredMixin,DetailView):
    template_name = 'doctor-detail.html'
    model = Doctor
    login_url = 'hospital:login'
    redirect_field_name = 'doctors-detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        doc_id = self.kwargs['pk']
        doctor_obj = Doctor.objects.get(pk=doc_id)
        context['doctor_obj']  = doctor_obj

        return context
 
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            patient = self.request.user
            image = Patient.objects.get(patient=patient)
            print('img_ur',image)
            context['image'] = image
            return context


class PatientProfileView(LoginRequiredMixin,TemplateView):
    next_page  = 'hospital:patient-profile.html'
    template_name = 'patient-profile.html'
    login_url = 'hospital:login'
    redirect_field_name = 'patient-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = Appointment.objects.filter(patient=self.request) 
        appointment_item =AppointmentItem.objects.filter(appointment__in=appointment)
        patient = self.request.user
        context['appointment_item'] = appointment_item
        context['patient'] = patient
        return context

class ShowAppointmentView(LoginRequiredMixin,TemplateView):
    template_name = 'appointment.html'
    login_url = 'hospital:login'
    redirect_field_name = 'appointment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doc_id = self.kwargs['pk']
        doc_obj = Doctor.objects.get(id=doc_id)
        patient = self.request.user
        print('patient',patient)
        context['doc_obj'] = doc_obj
        context['patient'] = patient
        return context

        

class Booked(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        doc_id = self.kwargs['id']
        doc_obj = Doctor.objects.get(id=doc_id)
        print(doc_obj)
        reason = 'checkup'
        due = '2022-01-05'  
        appointment_id = self.request.session.get('appointment_id',None)
        print('aap id',appointment_id)
        if appointment_id:
            appointment_obj = Appointment.objects.get(id=appointment_id)
            this_doc_in_appointments = appointment_obj.appointmentitem_set.filter(
                doctor=doc_obj)
            print('in cart',this_doc_in_appointments)
            if this_doc_in_appointments.exists():
                    raise ValidationError(self.request,'appointment already scheduled')
            else:
                appointment_item = AppointmentItem.objects.create(
                    appointment = appointment_obj,doctor=doc_obj,due=due,reason=reason
                )
                print('lll',appointment_item)
        else:
            appointment_obj = Appointment.objects.create(
                patient=str(self.request.user)

            )
            messages.add_message(self.request,messages.SUCCESS,'Appointment made successfully')
            print('obj',appointment_obj)
            self.request.session['appointment_id'] = appointment_obj.id
            appointment_item = AppointmentItem.objects.create(
                appointment = appointment_obj,doctor=doc_obj,due=due,reason=reason
                
            )
            print(appointment_item)
            appointment_obj.save()

        return context

    
class AboutView(TemplateView):
    template_name = 'hospital:about'

class DepartmentView(TemplateView):
    template_name = 'news.html'


class NewsView(TemplateView):
    template_name = 'home.html'

class NewsDetailView(TemplateView):
    template_name = 'news-detail.html'
