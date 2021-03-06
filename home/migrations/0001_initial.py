# Generated by Django 2.0.10 on 2022-01-27 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150)),
                ('former_surname', models.CharField(blank=True, max_length=120, null=True)),
                ('also_known_as_given_name', models.CharField(blank=True, max_length=120, null=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')], max_length=1)),
                ('school_id_number', models.CharField(max_length=150)),
                ('phone_number_home', models.CharField(blank=True, max_length=14, null=True)),
                ('phone_number_cell', models.CharField(blank=True, max_length=14, null=True)),
                ('email_address', models.EmailField(max_length=150)),
                ('mailing_address', models.EmailField(blank=True, max_length=150, null=True)),
                ('city_province', models.CharField(blank=True, max_length=150, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=150, null=True)),
                ('asn', models.CharField(blank=True, max_length=150, null=True)),
                ('aboriginal_status', models.CharField(blank=True, choices=[('Status Indian/First Nations', 'Status Indian/First Nations'), ('Non-Status Indian/First Nations', 'Non-Status Indian/First Nations'), ('Metis', 'Metis'), ('Inuit', 'Inuit')], max_length=100, null=True)),
                ('legal_status', models.CharField(blank=True, choices=[('Canadian', 'Canadian'), ('Permanent Resident', 'Permanent Resident'), ('Student Visa', 'Student Visa'), ('Other Visa (e.g. Working Visa)', 'Other Visa (e.g. Working Visa)'), ('Non-Canadian, no visa status', 'Non-Canadian, no visa status'), ('Not Reported/Unknown', 'Not Reported/Unknown')], max_length=100, null=True)),
                ('enrolment_start_date', models.DateField(blank=True, null=True)),
                ('enrolment_end_date', models.DateField(blank=True, null=True)),
                ('enrolment_actual_end', models.DateField(blank=True, null=True)),
                ('enrolment_grad_code', models.CharField(blank=True, max_length=120, null=True)),
                ('enrolment_jp_code', models.CharField(blank=True, max_length=120, null=True)),
                ('enrolment_employer_name', models.TextField(blank=True, null=True)),
                ('enrolment_employer_contact', models.TextField(blank=True, null=True)),
                ('enrolment_notes', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Program')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Status')),
            ],
        ),
    ]
