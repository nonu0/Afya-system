from hospital.models import Patient

def delete_patient_data(patient_email):
    print('useremail',patient_email)
    if Patient.objects.filter(patient=patient_email).exists():
        Patient.objects.filter(patient=patient_email).delete()