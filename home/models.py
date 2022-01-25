from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentInformation(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    former_surname = models.CharField(max_length=120)
    also_known_as_given_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(auto_now_add=False)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified')
    ]
    gender = models.CharField(max_length=1, choices=GENDER)
    school_id_number = models.CharField(max_length=150)
    phone_number_home = models.CharField(max_length=14)
    phone_number_cell = models.CharField(max_length=14)
    email_address = models.EmailField(max_length=150)
    mailing_address = models.EmailField(max_length=150)
    city_province = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    asn = models.CharField(max_length=150)
    AboriginalStatus = [
        ('Status Indian/First Nations', 'Status Indian/First Nations'),
        ('Non-Status Indian/First Nations', 'Non-Status Indian/First Nations'),
        ('Metis', 'Metis'),
        ('Inuit', 'Inuit')
    ]
    aboriginal_status = models.CharField(choices=AboriginalStatus, max_length=100)
    LegalStatus = [
        ('Canadian', 'Canadian'),
        ('Permanent Resident', 'Permanent Resident'),
        ('Student Visa', 'Student Visa'),
        ('Other Visa (e.g. Working Visa)', 'Other Visa (e.g. Working Visa)'),
        ('Non-Canadian, no visa status',
         'Non-Canadian, no visa status'),
        ('Not Reported/Unknown', 'Not Reported/Unknown')
    ]
    legal_status = models.CharField(choices=LegalStatus, max_length=100, blank=True, null=True)
    enrolment_start_date = models.DateField(auto_now_add=False)
    enrolment_end_date = models.DateField(auto_now_add=False)
    enrolment_actual_end = models.DateField(auto_now_add=False)
    enrolment_grad_code = models.CharField(max_length=120)
    enrolment_jp_code = models.CharField(max_length=120)
    enrolment_employer_name = models.TextField(blank=True, null=True)
    enrolment_employer_contact = models.TextField(blank=True, null=True)
    enrolment_notes = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
