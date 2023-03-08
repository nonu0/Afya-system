from django.db import models
from django.conf import settings
class Patient(models.Model):
    GENDER = (
        (1,'Male'),
        (2,'Female'),
        (3,'Undefined'),
    )
    ACT_STATUS = (
    (1,'Active'),
    (2,'Inactive'),
    (3,'Suspended'),
    )
    patient = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=250,null=True,blank=True)
    phone_no = models.IntegerField()
    gender = models.IntegerField(choices=GENDER,default=3)
    city = models.CharField(max_length=50)
    code = models.IntegerField(blank=True,null=True)
    phone_no = models.IntegerField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.username



class Doctor(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    experience = models.CharField(max_length=10)
    consultation_fee = models.IntegerField()

    def __str__(self):
        return 'Dr.' + str(self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(Patient,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',default='default.png',blank = True,null = True)

    def __str__(self) -> str:
        return self.user.username + " Profile picture"


class Appointment(models.Model):
    patient = models.CharField(max_length=50,unique=True,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return 'appointment' + str(self.id)

class AppointmentItem(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,blank=True,null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=True,null=True)
    due = models.DateTimeField(auto_now_add=False)
    reason = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 'appointment' + str(self.appointment.id) + 'appointment item' + str(self.id)
