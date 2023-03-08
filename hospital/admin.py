from django.contrib import admin
from hospital.models import Patient,Doctor,Appointment,AppointmentItem,UserProfile
from hospital.extras import delete_patient_data
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    # name of our db
    using = 'default'
    list_display = ('patient','first_name','last_name')
    list_display_link = ('patient','first_name','last_name')
    list_filter = ('patient','gender',)
    search_fields = ('first_name','last_name',)
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        # where to save
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using,**kwargs)

admin.site.register(Patient,HospitalAdmin)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(AppointmentItem)
admin.site.register(UserProfile)