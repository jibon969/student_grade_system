from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact-list/', views.contact_list, name='contact-list'),
    path('update-contact/<int:id>/', views.update_contact, name='update-contact'),
    path('delete-contact/<int:id>/', views.delete_contact, name='delete-contact'),
    path('replay-contact/', views.replay_contact, name='replay-contact'),
    path('download-contact-csv/', views.download_contact_csv, name='download-contact-csv')
]